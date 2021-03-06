from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Banana", {"fields": ("avatar", "gender", "bio")}),
    )

    list_display = (
        "username",
        "avatar",
        "gender",
        "bio",
        "birthdate",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email",
        "first_name",
        "last_name",
        "date_joined",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)


'''
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

'''


""" above things are same with this => admin.site.register(models.User, CustomUserAdmin)"""
