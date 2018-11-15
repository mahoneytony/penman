from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from orders import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
