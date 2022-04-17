from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """Abstract item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass


class Room(core_models.TimeStampedModel):

    """Room model definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    adress = models.CharField(max_length=140)
    guests = models.IntegerField()
    bed = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    roomtype = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name
