from django.db import models


class Object(models.Model):
    name = models.CharField(
        verbose_name='Название объекта', max_length=64
    )
    owner = models.ForeignKey(
        'users.User', verbose_name='Собственник',
        related_name='user_objects', on_delete=models.CASCADE,
    )
    address = models.OneToOneField(
        'address', related_name='object_by_address',
        verbose_name='Адрес', on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(
        default=False, verbose_name='Объявление активно',
    )
    view = models.PositiveIntegerField(
        default=0, verbose_name='Количество просмотров'
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    number_of_flat = models.PositiveSmallIntegerField(
        verbose_name='Количество этажей',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего обновления', auto_now=True
    )
    is_hidden = models.BooleanField(
        verbose_name='Объявление скрыто', default=False,
    )
    type = models.ForeignKey(
        'TypeOfObject', verbose_name='Тип', on_delete=models.SET_DEFAULT,
        related_name='objects_of_type', default=0,
    )

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{self.name}'


class BaseRoom(models.Model):
    rooms = models.PositiveSmallIntegerField(
        verbose_name='Количество комнат'
    )
    square = models.PositiveSmallIntegerField(
        verbose_name='Площадь'
    )
    adult = models.PositiveSmallIntegerField(
        verbose_name='Количество взрослых'
    )
    kid = models.PositiveSmallIntegerField(
        verbose_name='Количество детей'
    )
    sleeping_places = models.PositiveSmallIntegerField(
        verbose_name='Количество спальных мест'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего обновления', auto_now=True
    )

    class Meta:
        abstract = True


class IndependentObject(BaseRoom):
    base_object = models.OneToOneField(
        'Object', verbose_name='Базовый объект',
        on_delete=models.CASCADE, related_name='independent'
    )
    exact_address = models.OneToOneField(
        'ExactAddress', verbose_name='Точный адрес',
        on_delete=models.SET_NULL, related_name='independent',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Самостоятельный объект'
        verbose_name_plural = 'Самостоятельные объекты'

    def __str__(self):
        return f'Самостоятельный объект {self.base_object}'


class Room(BaseRoom):
    base_object = models.ForeignKey(
        'Object', verbose_name='Базовый объект',
        on_delete=models.CASCADE, related_name='rooms'
    )
    is_hidden = models.BooleanField(
        verbose_name='Номер скрыт', default=False,
    )

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return f'Номер {self.id} объекта {self.base_object}'


class TypeOfObject(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=25,
    )
    is_independent = models.BooleanField(
        verbose_name='Объект независимый'
    )

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объекта'

    def __str__(self):
        return f'{self.name} {self.is_independent}'
