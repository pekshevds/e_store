from django.utils.safestring import mark_safe
from django.contrib import admin
from wish_app.models import WishItem


@admin.register(WishItem)
class WishItemAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "good", "added", "preview",)
    list_filter = ("customer",)
    list_display_links = ("id", "customer", "good", "added",)

    def preview(self, obj: WishItem) -> str:
        if obj.good.image:
            return mark_safe(f'<img src="{obj.good.image.image.url}" style="max-height: 50px;">')
        return ""
