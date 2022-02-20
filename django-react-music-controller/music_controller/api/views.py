from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from api.models import Room
from .serializer import RoomSerializer


class RoomView(generics.CreateAPIView):
    queryset =  Room.objects.all()
    serializer_class = RoomSerializer
