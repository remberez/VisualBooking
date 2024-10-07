from django.db import models


class BasePriceList(models.Model):
    first_day = models.DateField(
        verbose_name='Начало срока',
    )
    last_day = models.DateField(
        verbose_name='Конец срока',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10, decimal_places=2,
    )

    class Meta:
        abstract = True


class IndependentPriceList(BasePriceList):
    object = models.ForeignKey(
        'IndependentObject', verbose_name='Объект', on_delete=models.CASCADE,
        related_name='price_list',
    )

    class Meta:
        verbose_name = 'Прайс лист самостоятельного объекта'
        verbose_name_plural = 'Прайс листы самостоятельного объекта'

    def __str__(self):
        return f'{self.object} {self.first_day} - {self.last_day}'


class PriceListOfRoom(BasePriceList):
    object = models.ForeignKey(
        'Room', verbose_name='Объект', on_delete=models.CASCADE,
        related_name='price_list',
    )

    class Meta:
        verbose_name = 'Прайс лист номера'
        verbose_name_plural = 'Прайс листы номеров'

    def __str__(self):
        return f'{self.object} {self.first_day} - {self.last_day}'
