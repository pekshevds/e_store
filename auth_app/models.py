from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    inn = models.CharField(verbose_name="ИНН", max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь (заказчик)"
        verbose_name_plural = "Пользователи (заказчики)"
