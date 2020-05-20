from django.db import models
from django_countries import countries

COUNTRY_CHOICES = tuple(countries)

class UserAccount(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=128, null=False)
    account_email = models.EmailField(max_length = 254, null=False, unique=True)
    country = models.CharField(choices=COUNTRY_CHOICES, null=False, max_length=75)
    activated = models.BooleanField(default=False)