from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        category = self.request.query_params.get('category')
        slug = self.request.query_params.get('slug')
        size = self.request.query_params.get('size')
        if category:
            queryset = Product.objects.filter(category__name=category)
        elif slug:
            queryset = Product.objects.filter(slug=slug)
        elif size:
            queryset = Product.objects.filter(size_eu=size)

        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})


class CategoryView(APIView):

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


