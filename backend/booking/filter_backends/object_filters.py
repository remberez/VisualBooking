import pdb

from django.db.models import Min, Max, Q
from rest_framework import filters
import django_filters
from booking.models.object import Object
from common import base_position


class ObjectFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.user.is_authenticated or request.user.position == base_position.USER_POSITION:
            return queryset.filter(
                is_active=True, is_hidden=False,
            )
        if request.user.position == base_position.OWNER_POSITION:
            return queryset.filter(
                Q(is_active=True) | Q(owner=request.user)
            )
        return queryset


class ObjectFilterSet(django_filters.FilterSet):
    first_day = django_filters.DateFilter(field_name='first_day', method='date_filter')
    last_day = django_filters.DateFilter(field_name='last_day', method='date_filter')

    class Meta:
        model = Object
        fields = ['first_day', 'last_day']

    def date_filter(self, queryset, name, value):
        first_day = self.data.get('first_day')
        last_day = self.data.get('last_day')

        if first_day and last_day:
            queryset = queryset.annotate(
                first_day=Min(
                    'price_list__first_day'
                ),
                last_day=Max(
                    'price_list__last_day'
                )
            ).filter(first_day__lte=first_day, last_day__gte=last_day)

        return queryset
