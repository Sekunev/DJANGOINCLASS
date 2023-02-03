from rest_framework import serializers
from .models import *
from datetime import datetime
import pytz

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id",'name')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", 'name', 'image')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    # createds = serializers.toLocaleString()
    createds = serializers.SerializerMethodField('oluşturulmaTarihi')
    updated = serializers.SerializerMethodField('guncellenmeTarihi')
    class Meta:
        model = Product
        fields = ("id", 'name','category', 'category_id', 'brand', 'brand_id', 'stock', 'createds', 'updated')

    def oluşturulmaTarihi(self, obj):
        date_string = str(obj.createds)
        date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f%z')
        timezone = pytz.timezone("Europe/Istanbul")
        local_time = date_object.astimezone(timezone)
        new_format = local_time.strftime('%Y-%m-%d %H:%M')
        # print(new_format)
        return new_format

    def guncellenmeTarihi(self, obj):
        date_string = str(obj.updated)
        date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f%z')
        timezone = pytz.timezone("Europe/Istanbul")
        local_time = date_object.astimezone(timezone)
        new_format = local_time.strftime('%Y-%m-%d %H:%M')
        # print(new_format)
        return new_format


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('name','phone','address', 'image')

class PurchasesSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    createds = serializers.SerializerMethodField()

    class Meta:
        model = Purchases
        fields = ("id", "user", "firm", "product", "brand", "quantity", "price", "price_total","category", 'createds')

    def get_product(self, obj):
        products = Product.objects.filter(id=obj.product_id).values()
        category_id= products[0]["category_id"]
        return list(Product.objects.filter(id=category_id).values())[0]["name"]
        
    def get_category(self,obj):
        products = Product.objects.filter(id=obj.product_id).values()
        # print(products)
        category_id= products[0]["category_id"]
        return list(Category.objects.filter(id=category_id).values())

    def get_createds(self,obj):
        products = Product.objects.filter(id=obj.product_id).values()
        print(products)
        purchase_id= products[0]["id"]
        return list(Product.objects.filter(id=purchase_id).values())[0]["createds"]



class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ("id", 'user', 'product', 'brand', 'quantity', 'price', 'price_total')
        # exclude = ('quantity',)