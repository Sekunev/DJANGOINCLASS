from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name', 'image')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ('name','category', 'category_id', 'brand', 'brand_id', 'stock', 'createds', 'updated')

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('name','phone','address', 'image')

class PurchasesSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Purchases
        fields = ("id", "user", "firm", "product", "brand", "quantity", "price", "price_total","category")
        
    def get_category(self,obj):
        products = Product.objects.filter(id=obj.product_id).values()
        print(products)
        category_id= products[0]["category_id"]
        return list(Category.objects.filter(id=category_id).values())[0]["name"]



class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('user', 'product', 'brand', 'quantity', 'price', 'price_total')
        # exclude = ('quantity',)