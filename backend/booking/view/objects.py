from django.db import IntegrityError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from common.mixins.view_mixins import CRUDViewSet
from common.pagination import BasePagination
from booking.serializers import objects as object_serializers
from common import permisions as custom_permissions
from booking.models.object import Object
from booking.serializers import media as media_serializers
from booking.filter_backends.object_filters import ObjectFilterSet, ObjectFilter
from rest_framework.permissions import IsAuthenticated


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
    add_images_object=extend_schema(
        summary='Добавить изображения к объекту',
        tags=['Объекты'],
    ),
    add_videos_object=extend_schema(
        summary='Добавить ссылки на видео к объекту',
        tags=['Объекты'],
    ),
    add_to_favorites=extend_schema(
        summary='Добавить объект в избранное',
        tags=['Объекты', 'Пользователи']
    )
)
class ObjectView(CRUDViewSet):
    multi_serializer_class = {
        'create': object_serializers.ObjectCreateSerializer,
        'add_images_object': media_serializers.ObjectImageSerializer,
        'add_videos_object': media_serializers.ObjectVideoSerializer,
        'list': object_serializers.ObjectListSerializer,
    }
    multi_permission_classes = {
        'create': (custom_permissions.IsOwnerPosition | custom_permissions.IsAdmin,),
        'add_images_object': (custom_permissions.IsOwnerOfObject,),
        'add_videos_object': (custom_permissions.IsOwnerOfObject,),
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'delete': (custom_permissions.IsOwnerOfObject | custom_permissions.IsAdmin),
        'add_to_favorites': (IsAuthenticated,)
    }
    queryset = Object.objects.all()

    filter_backends = (
        ObjectFilter,
        OrderingFilter,
        DjangoFilterBackend,
    )

    filterset_class = ObjectFilterSet
    ordering = ('id',)

    pagination_class = BasePagination

    def add_media(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'object_instance': instance})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(
        detail=True, methods=['post']
    )
    def add_images_object(self, request, *args, **kwargs):
        return self.add_media(request, args, kwargs)

    @action(
        detail=True, methods=['post']
    )
    def add_videos_object(self, request, *args, **kwargs):
        return self.add_media(request, args, kwargs)

    @action(
        detail=True, methods=['get']
    )
    def add_to_favorites(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data='Объект не найден')
        try:
            request.user.favorites_objects.add(obj)
        except IntegrityError:
            return Response(status=status.HTTP_208_ALREADY_REPORTED, data='Объект уже находится в избранном')
        return Response(status=status.HTTP_201_CREATED)
