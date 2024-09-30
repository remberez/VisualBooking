import pdb

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from common.mixins.view_mixins import CRUDViewSet
from users.serializers import user


@extend_schema_view(
    create=extend_schema(
        summary='Регистрация',
        tags=['Пользователи'],
    ),
    list=extend_schema(
        summary='Список пользователей',
        tags=['Пользователи'],
    ),
    retrieve=extend_schema(
        summary='Пользователь по id',
        tags=['Пользователи'],
    ),
    destroy=extend_schema(
        summary='Удаление пользователя',
        tags=['Пользователи'],
    ),
    partial_update=extend_schema(
        summary='Обновить пользователя',
        tags=['Пользователи'],
    )
)
class UserView(CRUDViewSet):
    multi_serializer_class = {
        'create': user.UserRegistrationSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        errors = []
        for err in serializer.errors.values():
            errors.append(err)
        return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)
