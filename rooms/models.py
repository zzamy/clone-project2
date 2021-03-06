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
    """Room-type model definition"""

    class Meta:
        verbose_name = "Room type"
        ordering = ["created"]


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class Amenity(AbstractItem):
    """Amenity model definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class HouseRule(AbstractItem):
    """House Rules model definition"""

    class Meta:
        verbose_name = "House Rule"


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
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )
    roomtype = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    photo = models.ImageField()
    room = models.ForeignKey(Room, related_name="photos", on_delete=models.CASCADE)
    # Room ?????? CASCADE ?????? : ?????? ??? ????????? ????????? ????????? ???????????????

    def __str__(self):
        return self.caption
