from django.db import models
from datetime import datetime


class Directory(models.Model):

    name = models.CharField(verbose_name="Наименование", max_length=150, null=False, blank=False, db_index=True)
    comment = models.CharField(verbose_name="Комментарий", max_length=1024, null=False, blank=True, default="")
    is_mark = models.BooleanField(verbose_name="Пометка", default=False)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True
        ordering = ["id"]


class Document(models.Model):

    comment = models.CharField(verbose_name="Комментарий", max_length=1024, null=False, blank=True, default="")
    is_mark = models.BooleanField(verbose_name="Пометка", default=False)
    date = models.DateTimeField(verbose_name="Дата", default=datetime.now())
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self) -> str:
        formated_date = datetime.strftime(self.date, "%m.%d.%Y")
        return f'{self.id} от {formated_date}'

    class Meta:
        abstract = True
        ordering = ["id"]
