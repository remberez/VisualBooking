# Generated by Django 5.1 on 2024-09-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='floor',
            field=models.PositiveSmallIntegerField(verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='object',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
