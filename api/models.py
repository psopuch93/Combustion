from django.contrib.auth.models import User
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
    name_choices = (
        ('All', 'All'),
        ('Shoes', 'Shoes'),
        ('Tops', 'Tops'),
        ('Pants', 'Pants'),
        ('Dresses', 'Dresses'),
        ('Pants', 'Pants')
    )
    name = models.CharField(max_length=255, db_index=True, choices=name_choices, default='')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=256, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, default=None)
    brand = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    product_image = ResizedImageField(size=[500, 300], upload_to='product_images/', blank=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField(default=0, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-date_created',)

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.product_image.url}" '
                         f'width = "{self.product_image.width}" '
                         f'height = "{self.product_image.height }"/>')

