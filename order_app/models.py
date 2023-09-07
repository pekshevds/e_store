from django.db import models
from index_app.models import Document


class Order(Document):

    class Meta:
        verbose_name = "Заказ клиента"
        verbose_name_plural = "Заказы клиентов"
