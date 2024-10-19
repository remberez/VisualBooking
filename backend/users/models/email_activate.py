from django.db import models


class EmailActivate(models.Model):
    user = models.OneToOneField(
        'User', related_name='email_activate',
        verbose_name='Пользователь', on_delete=models.CASCADE
    )
    code = models.CharField(
        verbose_name='Код', max_length=6
    )

    class Meta:
        verbose_name = 'Активация почты'
        verbose_name_plural = 'Активация почты'
