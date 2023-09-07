from django.contrib import admin
from order_app.models import Order
from order_app.models import OrderItem


# class OrderItemInLine(admin.StackedInline):
class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "customer", "comment", "amount",)
    list_filter = ("customer",)
    list_display_links = ("id", "date",)
    inlines = [OrderItemInLine]


admin.site.register(Order, OrderAdmin)
