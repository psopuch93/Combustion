from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'company', 'address', 'postcode', 'phone_number', 'date_created')


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

