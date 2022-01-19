from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from apps.inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "price")
