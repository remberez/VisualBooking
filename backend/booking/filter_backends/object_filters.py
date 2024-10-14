from django.db.models import Min, Q, Prefetch, Case, When, DecimalField, F, Max
from rest_framework import filters
import django_filters
from booking.models.object import Object, Room
from booking.models.price_list import PriceListOfRoom, IndependentPriceList
from common import base_position


def get_price_filter(first_day, last_day):
    independent_filters = Q()
    rooms_filters = Q()

    if first_day:
        independent_filters |= Q(
            independent__price_list__first_day__lte=first_day,
            independent__price_list__last_day__gte=first_day
        )
        rooms_filters |= Q(
            rooms__price_list__first_day__lte=first_day,
            rooms__price_list__last_day__gte=first_day
        )

    if last_day:
        independent_filters |= Q(
            independent__price_list__first_day__lte=last_day,
            independent__price_list__last_day__gte=last_day
        )
        rooms_filters |= Q(
            rooms__price_list__first_day__lte=last_day,
            rooms__price_list__last_day__gte=last_day
        )

    return independent_filters, rooms_filters


def annotate_price(queryset, first_day, last_day):
    independent_filters = rooms_filters = None
    if first_day and last_day:
        independent_filters, rooms_filters = get_price_filter(first_day, last_day)
    return queryset.annotate(
        min_price=Case(
            When(
                independent__isnull=False,
                then=Min('independent__price_list__price', filter=independent_filters),
            ),
            When(
                independent__isnull=True,
                then=Min('rooms__price_list__price', filter=rooms_filters),
            ),
            output_field=DecimalField(),
        ),
    )


def annotate_people(queryset):
    queryset = queryset.annotate(
        max_adults=Case(
            When(independent__isnull=False, then=F('independent__adult')),
            When(independent__isnull=True, then=Max('rooms__adult')),
        ),
        max_kids=Case(
            When(independent__isnull=False, then=F('independent__kid')),
            When(independent__isnull=True, then=Max('rooms__kid')),
        )
    )
    return queryset


def define_date_filters(first_day, last_day):
    rooms_filters = Q()
    price_list_filters = Q()
    if first_day and last_day:
        rooms_filters = Q(
            Q(price_list__first_day__lte=first_day, price_list__last_day__gte=first_day) |
            Q(price_list__first_day__lte=last_day, price_list__last_day__gte=last_day)
        )
        price_list_filters = Q(
            Q(first_day__lte=first_day, last_day__gte=first_day) |
            Q(first_day__lte=last_day, last_day__gte=last_day)
        )
    return rooms_filters, price_list_filters


class ObjectFilter(filters.BaseFilterBackend):

    def position_filter(self, request, queryset):
        if not request.user.is_authenticated or request.user.position == base_position.get_user_position():
            return queryset.filter(
                is_active=True, is_hidden=False,
            )
        if request.user.position == base_position.get_owner_position():
            return queryset.filter(
                Q(is_active=True, is_hidden=False) | Q(owner=request.user)
            )
        return queryset

    def list_filter(self, request, queryset, view):
        first_day = request.query_params.get('first_day')
        last_day = request.query_params.get('last_day')

        rooms_filters, price_list_filters = define_date_filters(first_day, last_day)
        queryset = queryset.select_related(
            'owner', 'address', 'type', 'independent', 'independent__exact_address', 'address__city',
        ).prefetch_related(
            Prefetch('rooms', queryset=Room.objects.filter(rooms_filters).distinct().prefetch_related(
                    Prefetch('price_list', queryset=PriceListOfRoom.objects.filter(price_list_filters))
                )
            ),
            Prefetch(
                'independent__price_list', queryset=IndependentPriceList.objects.filter(price_list_filters)
            )
        )
        return self.position_filter(request, annotate_price(annotate_people(queryset), first_day, last_day))

    def filter_queryset(self, request, queryset, view):
        action = view.action
        if action == 'list':
            return self.list_filter(request, queryset, view)


class ObjectFilterSet(django_filters.FilterSet):
    first_day = django_filters.DateFilter(field_name='first_day', method='first_day_filter')
    last_day = django_filters.DateFilter(field_name='last_day', method='last_day_filter')
    city = django_filters.CharFilter(field_name='address__city', lookup_expr='name')
    price = django_filters.RangeFilter(field_name='min_price')
    sea_distance = django_filters.NumberFilter(field_name='address__sea_distance', lookup_expr='lte')
    adults = django_filters.NumberFilter(field_name='max_adults', lookup_expr='gte')
    kids = django_filters.NumberFilter(field_name='max_kids', lookup_expr='gte')

    class Meta:
        model = Object
        fields = ['first_day', 'last_day', 'city', 'type']

    def filter_by_date(self, queryset, first_day=None, last_day=None):
        independent_filters, rooms_filters = get_price_filter(first_day, last_day)
        return queryset.filter(rooms_filters | independent_filters).distinct()

    def first_day_filter(self, queryset, name, value):
        if not self.data.get('last_day'):
            return queryset

        return self.filter_by_date(queryset, first_day=value)

    def last_day_filter(self, queryset, name, value):
        if not self.data.get('first_day'):
            return queryset

        return self.filter_by_date(queryset, last_day=value)
