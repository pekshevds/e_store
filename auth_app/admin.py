from django.contrib import admin
from auth_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
