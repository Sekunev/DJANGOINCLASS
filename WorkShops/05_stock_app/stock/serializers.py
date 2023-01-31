from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ('name','category', 'category_id', 'brand', 'brand_id', 'stock')

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('name','phone','address')

class PurchasesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchases
        fields = ('user','firm','product', 'brand', 'quantity', 'price', 'price_total')



class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('user', 'product', 'brand', 'quantity', 'price', 'price_total')
        # exclude = ('quantity',)