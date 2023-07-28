from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'company', 'address',
                    'postcode', 'phone_number', 'date_created', 'date_updated',)
    list_filter = ("company",)
    search_fields = ("lastname__startswith", "company__startswith")

    class Meta:
        ordering = ("name", "lastname")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("name", "description", "slug")
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ("name",)
    search_fields = ("name__startswith",)

    class Meta:
        ordering = ("name", "lastname")


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'in_stock',
                    'date_created', 'date_updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['img_preview']
