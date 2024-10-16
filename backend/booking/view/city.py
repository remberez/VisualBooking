from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import AllowAny
from booking.models.address import City
from common.mixins.view_mixins import CRUDViewSet
from booking.serializers.city import CityListRetrieveSerializer, CityCreateUpdateSerializer
from common.pagination import BasePagination
from common.permisions import IsAdmin
from rest_framework.filters import OrderingFilter


@extend_schema_view(
    list=extend_schema(
        summary='Список городов',
        tags=['Города'],
    ),
    create=extend_schema(
        summary='Добавить город',
        tags=['Города'],
    ),
    retrieve=extend_schema(
        summary='Один город',
        tags=['Города'],
    ),
    destroy=extend_schema(
        summary='Удалить город',
        tags=['Города'],
    ),
    partial_update=extend_schema(
        summary='Обновить город',
        tags=['Города'],
    ),
)
class CityView(CRUDViewSet):
    multi_serializer_class = {
        'list': CityListRetrieveSerializer,
        'create': CityCreateUpdateSerializer,
        'retrieve': CityListRetrieveSerializer,
        'partial_update': CityCreateUpdateSerializer,
    }
    multi_permission_classes = {
        'list': (AllowAny,),
        'create': (IsAdmin,),
        'retrieve': (AllowAny,),
        'destroy': (IsAdmin,),
        'partial_update': (IsAdmin,),
    }
    queryset = City.objects.all()

    filter_backends = (
        OrderingFilter,
    )
    pagination_class = BasePagination
    ordering = ('id',)
