from rest_framework import serializers
from .models import *
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()  # read only
    class Meta:
        model = Category
        fields = ("id",'name','product_count')

    def get_product_count(self, obj):
        print(obj)  # Clothing Jewelery --> Category modelindeki name'ler
        print(Product.objects.filter(category_id=obj.id))  # <QuerySet [<Product: Terrex - Clothing>]>
        return Product.objects.filter(category_id=obj.id).count()  # category_id --> product tablosundaki category fieldi DB'de category_id olarak kayıtlı. o yüzden.

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ("id", "name", "category", "category_id", "brand", "brand_id","stock")
        read_only_fields = ("stock",) # stock purchases ve sales deki değişikliklerle değişecek. O yüzden burada read_only. prodoct' ile post da yapsam artık stock'u değiştiremeyeceğim.

"""    #! name params(query)'si ile category sorgusu yaptığımda product'larda dönsün istiyorum. 
http://127.0.0.1:8000/stock/categories/?search=&name=Clothing  --> endpointi çağrıldığında aşağıdaki veri döner.

[
    {
        "id": 1,
        "name": "Clothing",
        "product_count": 1,
        "products": [
            {
                "id": 1,
                "name": "Terrex",
                "stock": 10,
                "createds": "2023-02-02T18:56:22.376890Z",
                "updated": "2023-02-02T18:56:22.377890Z",
                "category": 1,
                "brand": 1
            }
        ]
    }
"""
class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)  # related name deki products
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ("id",'name','product_count', 'products')

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count() 

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image'
        )


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('id','name','phone','address', 'image')

class PurchasesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()
    time_hour = serializers.SerializerMethodField()
    createds = serializers.SerializerMethodField()

    class Meta:
        model = Purchases
        fields = (
            "id",
            "user",
            "user_id",
            "category",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            "time_hour",
            "createds",
        )
        # price_totalı create metodunu override ederek veya signal ile oluşturabiliriz. Biz signal'i tercih ettik.

    def get_category(self, obj):
        print(obj.product.category.name)
        product = Product.objects.get(id=obj.product_id)
        return Category.objects.get(id=product.category_id).name
    # pratik yöntem
    # def get_category(self, obj):
    #     return obj.product.category.name

    def get_time_hour(self, obj):
        return datetime.strftime(obj.createds, "%H:%M")

    def get_createds(self, obj):
        return datetime.strftime(obj.createds, "%d-%m-%Y")

class SalesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() 
    brand = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    # category = serializers.SerializerMethodField()
    time_hour = serializers.SerializerMethodField()
    createds = serializers.SerializerMethodField()
    
    class Meta:
        model = Sales
        fields = (
            "id",
            "user",
            "user_id",
            # "category",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            "time_hour",
            "createds",
        )
        
    # def get_category(self, obj):
    #     return obj.product.category.name
    
    def get_time_hour(self, obj):
        return datetime.strftime(obj.createds, "%H:%M")
    
    def get_createds(self, obj):
        return datetime.strftime(obj.createds, "%d,%m,%Y")
    