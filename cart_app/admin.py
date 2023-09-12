from django.utils.safestring import mark_safe
from django.contrib import admin
from cart_app.models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "good", "qnt", "added", "preview",)
    list_filter = ("customer",)
    list_display_links = ("id", "customer", "good", "qnt", "added",)

    def preview(self, obj: CartItem) -> str:
        if obj.good.image:
            return mark_safe(f'<img src="{obj.good.image.image.url}" style="max-height: 50px;">')
        return ""
