from django.db import models
from index_app.models import Document
from catalog_app.models import Good
from auth_app.models import User


class Order(Document):

    CREATED = "created"
    PAID = "paid"
    SHIPPED = "shipped"
    CONFIRMED = "confirmed"

    STATUS_CHOICES = [
        (CREATED, "Создан"),
        (PAID, "Оплачен"),
        (SHIPPED, "Доставлен"),
        (CONFIRMED, "Подтвержден"),
    ]

    class Meta:
        verbose_name = "Заказ клиента"
        verbose_name_plural = "Заказы клиентов"

    status = models.CharField(verbose_name="Статус", max_length=12, choices=STATUS_CHOICES, default=CREATED, 
                              null=True, blank=True)
    amount = models.DecimalField(verbose_name="Сумма", max_digits=15, decimal_places=2,
                                 null=True, blank=True, default=0, editable=False)
    customer = models.ForeignKey(User, verbose_name="Заказчик", on_delete=models.PROTECT, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.amount = sum([item.amount for item in self.items.all()])
        super().save(*args, **kwargs)


class OrderItem(models.Model):

    class Meta:
        verbose_name = "Строка заказ клиента"
        verbose_name_plural = "Строки заказа клиента"

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    good = models.ForeignKey(Good, verbose_name="Товар", on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name="Цена", max_digits=15, decimal_places=2,
                                null=True, blank=True, default=0)
    qnt = models.DecimalField(verbose_name="Количество", max_digits=15, decimal_places=3,
                              null=True, blank=True, default=0)
    amount = models.DecimalField(verbose_name="Сумма", max_digits=15, decimal_places=2,
                                 null=True, blank=True, default=0)

    def __str__(self) -> str:
        return f'{self.order} - {self.id}'

    def save(self, *args, **kwargs):
        self.amount = self.qnt * self.price
        super().save(*args, **kwargs)
