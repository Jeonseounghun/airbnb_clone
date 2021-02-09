from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGAUGE_ENGLISH = "en"
    LANGAUGE_KOREAN = "ko"

    LANGAUGE_CHOICE = (
        (LANGAUGE_ENGLISH, "english"),
        (LANGAUGE_KOREAN, "korean"),
    )

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"

    CURRENCY_CHOICE = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)

    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    langauge = models.CharField(choices=LANGAUGE_CHOICE, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
