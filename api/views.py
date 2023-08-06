from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__name=category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count': len(serializer.data),'data':serializer.data})


class CategoryView(APIView):

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


