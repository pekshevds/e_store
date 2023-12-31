# Generated by Django 4.2.5 on 2023-09-08 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0008_order_status_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 15, 30, 29, 294155), null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_mark',
            field=models.BooleanField(default=False, null=True, verbose_name='Пометка'),
        ),
    ]
