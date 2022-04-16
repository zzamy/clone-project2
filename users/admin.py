from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom user admin"""

    list_display = (
        "username",
        "avatar",
        "gender",
        "bio",
        "birthdate",
        "language",
        "currency",
        "superhost",
        "email",
        "first_name",
        "last_name",
        "date_joined",
    )

    list_filter = ("language",)


""" above things are same with this => admin.site.register(models.User, CustomUserAdmin)"""
