from django.contrib import admin
from catalog_app.models import Good
from catalog_app.models import Category

class GoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category",)
    list_display_links = ("id", "name",)
    list_filter = ("category",)
    search_fields = ("name", )

admin.site.register(Good, GoodAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name", )
    search_fields = ("name", )

admin.site.register(Category, CategoryAdmin)
