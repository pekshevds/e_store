from django.contrib import admin
from order_app.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "comment", )
    list_display_links = ("id", "date",)

admin.site.register(Order, OrderAdmin)
