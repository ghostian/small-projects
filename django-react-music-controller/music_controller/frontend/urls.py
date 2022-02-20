"""
Created by cyborgoat at 2022/2/20
Email: cyborgoat@outlook.com

Description
-----------
"""

from django.urls import path

from .views import index

urlpatterns = [
    path('', index),
]
