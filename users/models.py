from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, region="RU")
    description = models.CharField(max_length=100, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name + " " + self.last_name
