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

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Difinition"""

    pass
