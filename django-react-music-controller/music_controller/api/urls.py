"""
Created by cyborgoat at 2022/2/20
Email: cyborgoat@outlook.com

Description
-----------

"""
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()),
]
