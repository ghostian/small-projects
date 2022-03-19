"""
Created by cyborgoat at 2022/3/19
Email: cyborgoat@outlook.com

Description
-----------

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/',views.getProducts,name="products")
]
