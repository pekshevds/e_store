from django.utils.safestring import mark_safe
from django.contrib import admin
from catalog_app.models import Good
from catalog_app.models import Category
from catalog_app.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview",)
    list_display_links = ("id", "name",)
    search_fields = ("name", )

    def preview(self, obj: Image) -> str:
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;">')


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "preview", "art",)
    list_display_links = ("id", "name", "art",)
    list_filter = ("category",)
    search_fields = ("name", "art",)

    def preview(self, obj: Good) -> str:
        if obj.image:
            return mark_safe(f'<img src="{obj.image.image.url}" style="max-height: 50px;">')
        return ""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name", )
    search_fields = ("name", )
