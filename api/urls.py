from django.urls import path
from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
]
