# Generated by Django 4.2.5 on 2023-09-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь (заказчик)', 'verbose_name_plural': 'Пользователи (заказчики)'},
        ),
        migrations.AddField(
            model_name='user',
            name='inn',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='ИНН'),
        ),
    ]
