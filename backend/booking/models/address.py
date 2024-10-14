from django.db import models


class Address(models.Model):
    city = models.ForeignKey(
        'City', verbose_name='Город', on_delete=models.CASCADE,
        related_name='addresses'
    )
    street = models.CharField(
        verbose_name='Улица', max_length=255,
    )
    house = models.PositiveSmallIntegerField(
        verbose_name='Номер дома', null=True, blank=True
    )
    sea_distance = models.PositiveSmallIntegerField(
        verbose_name='Расстояние до моря'
    )
    latitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=8, decimal_places=6
    )
    longitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=8, decimal_places=6,
    )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city} {self.street} {self.house}'


class ExactAddress(models.Model):
    entrance = models.PositiveSmallIntegerField(
        verbose_name='Номер подъезда', null=True, blank=True
    )
    apartment = models.PositiveSmallIntegerField(
        verbose_name='Номер квартиры', null=True, blank=True
    )
    floor = models.PositiveSmallIntegerField(
        verbose_name='Номер квартиры', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Точный адрес'
        verbose_name_plural = 'Точные адреса'

    def __str__(self):
        return f'{self.entrance} {self.apartment} {self.floor}'


class City(models.Model):
    name = models.CharField(
        verbose_name='Название города', max_length=35,
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'
