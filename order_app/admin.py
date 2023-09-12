from django.contrib import admin
from order_app.models import Order
from order_app.models import OrderItem


# class OrderItemInLine(admin.StackedInline):
class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "customer", "status", "comment", "amount",)
    list_filter = ("status", "customer",)
    list_display_links = ("id", "date",)
    inlines = [OrderItemInLine]
