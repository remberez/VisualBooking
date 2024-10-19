import secrets
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from common.mixins.view_mixins import CRUDViewSet
from users.models.email_activate import EmailActivate
from users.serializers import user as user_serializers
from rest_framework import permissions, status
from common import permisions as custom_permissions
from common.pagination import BasePagination
from users.tasks import send_code

User = get_user_model()


@extend_schema_view(
    create=extend_schema(
        summary='Регистрация',
        tags=['Пользователи'],
        description='Регистрация только для не авторизированных пользователей. '
                    '(то-есть без заголовка authentication в запросе'
    ),
    list=extend_schema(
        summary='Список пользователей',
        tags=['Пользователи'],
        description='Список пользователей, информация о пользователях короткая,'
                    'для полной информации есть другая точка. Доступна только админу.'
    ),
    retrieve=extend_schema(
        summary='Детальная информация о пользователе.',
        tags=['Пользователи'],
        description='Детальная информация о пользователе по id. Доступна только админу.'
    ),
    destroy=extend_schema(
        summary='Удаление пользователя',
        tags=['Пользователи'],
        description='Доступна только админу.'
    ),
    partial_update=extend_schema(
        summary='Обновить пользователя',
        tags=['Пользователи'],
        description='Обновлять можно почту, телефон, ФИО. Доступно владельцу аккаунта или админу'
    ),
    send_code=extend_schema(
        summary='Отправить код с подтверждением',
        tags=['Пользователи'],
    ),
    activate_email=extend_schema(
        summary='Подтвердить код',
        tags=['Пользователи']
    )
)
class UserView(CRUDViewSet):
    queryset = User.objects.all()
    multi_serializer_class = {
        'create': user_serializers.UserRegistrationSerializer,
        'list': user_serializers.UserListSerializer,
        'retrieve': user_serializers.UserDetailSerializer,
        'partial_update': user_serializers.UserUpdateSerializer,
        'activate_email': user_serializers.ActivateEmailSerializer,
    }
    multi_permission_classes = {
        'create': (~permissions.IsAuthenticated,),
        'list': (custom_permissions.IsAdmin,),
        'retrieve': (custom_permissions.IsAdmin,),
        'partial_update': (custom_permissions.IsOwnerOfAccount | custom_permissions.IsAdmin,),
        'destroy': (custom_permissions.IsAdmin,),
        'send_code': (permissions.IsAuthenticated,),
        'activate_email': (permissions.IsAuthenticated,),
    }

    pagination_class = BasePagination

    @action(
        detail=True, methods=['get']
    )
    def send_code(self, request, *args, **kwargs):
        def generate_code():
            EmailActivate.objects.create(
                user=user,
                code=code
            )
            send_code.delay(user.email, code)

        user = self.get_object()
        if request.user == user and not request.user.mail_confirmed:
            code = secrets.token_hex(3)
            try:
                generate_code()
            except IntegrityError as e:
                EmailActivate.objects.filter(user=user).first().delete()
                generate_code()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(
        detail=False, methods=['post']
    )
    def activate_email(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
