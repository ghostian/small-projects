"""
Created by cyborgoat at 2022/3/22
Email: cyborgoat@outlook.com

Description
-----------

"""
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
