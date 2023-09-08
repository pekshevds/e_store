from django.db import models
from catalog_app.models import Good
from auth_app.models import User


class CartItem(models.Model):

    class Meta:
        verbose_name = "Строка корзины"
        verbose_name_plural = "Корзина"

    customer = models.ForeignKey(User, verbose_name="Заказчик", on_delete=models.PROTECT, null=True, blank=True)
    good = models.ForeignKey(Good, verbose_name="Товар", on_delete=models.PROTECT)
    qnt = models.DecimalField(verbose_name="Количество", max_digits=15, decimal_places=3,
                              null=True, blank=True, default=0)
    added = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.customer} - {self.good} - {self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
