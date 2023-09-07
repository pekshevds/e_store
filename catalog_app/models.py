from django.db import models
from index_app.models import Directory


class Good(Directory):
    category = models.ForeignKey("Category", verbose_name="Категория", related_name="goods",
                                 on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(Directory):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
