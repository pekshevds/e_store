# Generated by Django 4.2.5 on 2023-09-11 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0011_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 11, 19, 47, 5, 490146), null=True, verbose_name='Дата'),
        ),
    ]
