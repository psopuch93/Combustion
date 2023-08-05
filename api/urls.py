from django.urls import path
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('')
]
