from django.shortcuts import get_object_or_404
from .models import Category, Product
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import *
import json


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

