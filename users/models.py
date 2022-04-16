from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANG_KOR = "KOR"
    LANG_ENG = "ENG"
    LANG_CHOICE = (
        (LANG_KOR, "KOREAN"),
        (LANG_ENG, "ENGLISH"),
    )

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KWR"
    CURRENCY_CHOICE = (
        (CURRENCY_KRW, "KOREAN WON"),
        (CURRENCY_USD, "USD DOLLOR"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANG_CHOICE, null=True, max_length=10, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICE, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
