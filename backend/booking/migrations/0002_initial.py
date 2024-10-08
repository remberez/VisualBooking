# Generated by Django 5.1 on 2024-10-06 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_objects', to=settings.AUTH_USER_MODEL, verbose_name='Собственник'),
        ),
        migrations.AddField(
            model_name='independentobject',
            name='base_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='independent', to='booking.object', verbose_name='Базовый объект'),
        ),
        migrations.AddField(
            model_name='objectimage',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='booking.object', verbose_name='Объект'),
        ),
        migrations.AddField(
            model_name='objectvideo',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='booking.object', verbose_name='Объект'),
        ),
        migrations.AddField(
            model_name='room',
            name='base_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='booking.object', verbose_name='Базовый объект'),
        ),
        migrations.AddField(
            model_name='pricelistofroom',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_list', to='booking.room', verbose_name='Объект'),
        ),
        migrations.AddField(
            model_name='object',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='objects_of_type', to='booking.typeofobject', verbose_name='Тип'),
        ),
    ]
