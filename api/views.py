from django.shortcuts import get_object_or_404
from .models import Category, Product
from django.http import JsonResponse
import json


def all_products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)


def all_categories(request):
    categories = list(Category.objects.values())
    return JsonResponse(categories, safe=False)
