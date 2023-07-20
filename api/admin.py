from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'company', 'address', 'postcode', 'phone_number', 'date_created', 'date_updated')
    list_filter = ("company", )
    search_fields = ("lastname__startswith", "company__startswith")

    class Meta:
        ordering = ("name", "lastname")


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

    search_fields = ("name__startswith", "description__startswith")


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price')
    readonly_fields = ['img_preview']
