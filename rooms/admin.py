from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Difinition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Difinition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "adress",
                    "price",
                )
            },
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        (
            "Space",
            {
                "fields": (
                    "bed",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "More About The Space",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Last Details",
            {
                "fields": ("host",),
            },
        ),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "bed",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "roomtype",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    search_fields = ("=city", "host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Difinition"""

    pass
