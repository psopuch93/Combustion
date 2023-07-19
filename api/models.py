from django.db import models
# Phone number model fields
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    phone_number = PhoneNumberField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=200, blank=True)





