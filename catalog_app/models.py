from django.db import models
from index_app.models import Directory


class Image(Directory):
    image = models.ImageField(verbose_name="Изображение", upload_to="images/", null=False, blank=False)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Category(Directory):
    code_1c = models.CharField(verbose_name="Код 1С", max_length=11, null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Good(Directory):
    category = models.ForeignKey(Category, verbose_name="Категория", related_name="goods",
                                 on_delete=models.PROTECT, null=True, blank=True)
    image = models.ForeignKey(Image, verbose_name="Изображение", on_delete=models.PROTECT, null=True, blank=True)
    code_1c = models.CharField(verbose_name="Код 1С", max_length=11, null=True, blank=True, db_index=True)
    art = models.CharField(verbose_name="Артикул", max_length=25, null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
