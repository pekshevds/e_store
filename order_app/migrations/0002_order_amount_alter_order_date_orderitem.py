# Generated by Django 4.2.5 on 2023-09-07 04:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_alter_category_options_alter_good_options_and_more'),
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=15, null=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 7, 11, 29, 64277), verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Цена')),
                ('qnt', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='Количество')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Сумма')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog_app.good', verbose_name='Товар')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order_app.order')),
            ],
        ),
    ]
