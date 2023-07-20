from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import mark_safe
from django_resized import ResizedImageField


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=100, blank=True, unique=True)
    address = models.CharField(max_length=200, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    phone_number = PhoneNumberField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    description = models.CharField(max_length=100, blank=True)
    price = models.FloatField(null=False)
    product_image = ResizedImageField(size=[500, 300], upload_to='product_images/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def img_preview(self):
        return mark_safe(f'<img src = "{self.product_image.url}" '
                         f'width = "{self.product_image.width}" '
                         f'height = "{self.product_image.height }"/>')
