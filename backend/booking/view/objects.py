from drf_spectacular.utils import extend_schema_view, extend_schema
from common.mixins.view_mixins import CRUDViewSet
from common.pagination import BasePagination
from booking.serializers import objects as object_serializers
from common import permisions as custom_permissions


@extend_schema_view(
    create=extend_schema(
        summary='Создание объекта',
        tags=['Объекты'],
    ),
    list=extend_schema(
        summary='Список объектов',
        tags=['Объекты'],
    ),
    retrieve=extend_schema(
        summary='Детальная информация об объекте.',
        tags=['Объекты'],
    ),
    destroy=extend_schema(
        summary='Удаление объекта',
        tags=['Объекты'],
    ),
    partial_update=extend_schema(
        summary='Обновить объект',
        tags=['Объекты'],
    ),
)
class ObjectView(CRUDViewSet):
    multi_serializer_class = {
        'create': object_serializers.ObjectCreateSerializer,
    }
    multi_permission_classes = {
        'create': (custom_permissions.IsOwnerPosition | custom_permissions.IsAdmin,),
    }
    pagination_class = BasePagination
