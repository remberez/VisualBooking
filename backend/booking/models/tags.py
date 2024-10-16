from django.db import models


class Tag(models.Model):
    title = models.CharField(
        verbose_name='Заголовок', max_length=32
    )
    svg = models.ImageField(
        verbose_name='svg', upload_to='tags/',
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title
