from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    list_editable = (
        "is_staff",
        "is_superuser",
        "is_active",
    )

    ordering = ("id",)
