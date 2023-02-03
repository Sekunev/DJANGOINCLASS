from rest_framework import serializers
from .models import *
from datetime import datetime
import pytz

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
    class Meta:
        model = Product
        fields = "__all__"

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






# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = ("id", 'name', 'image')

# class ProductSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     category_id = serializers.IntegerField()
#     brand = serializers.StringRelatedField()
#     brand_id = serializers.IntegerField()
#     # createds = serializers.toLocaleString()
#     createds = serializers.SerializerMethodField('oluşturulmaTarihi')
#     updated = serializers.SerializerMethodField('guncellenmeTarihi')
#     class Meta:
#         model = Product
#         fields = ("id", 'name','category', 'category_id', 'brand', 'brand_id', 'stock', 'createds', 'updated')

#     def oluşturulmaTarihi(self, obj):
#         date_string = str(obj.createds)
#         date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f%z')
#         timezone = pytz.timezone("Europe/Istanbul")
#         local_time = date_object.astimezone(timezone)
#         new_format = local_time.strftime('%Y-%m-%d %H:%M')
#         # print(new_format)
#         return new_format

#     def guncellenmeTarihi(self, obj):
#         date_string = str(obj.updated)
#         date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f%z')
#         timezone = pytz.timezone("Europe/Istanbul")
#         local_time = date_object.astimezone(timezone)
#         new_format = local_time.strftime('%Y-%m-%d %H:%M')
#         # print(new_format)
#         return new_format


# class FirmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Firm
#         fields = ('name','phone','address', 'image')

# class PurchasesSerializer(serializers.ModelSerializer):
#     product = serializers.SerializerMethodField()
#     category = serializers.SerializerMethodField()
#     brand = serializers.StringRelatedField()
#     createds = serializers.SerializerMethodField()

#     class Meta:
#         model = Purchases
#         fields = ("id", "user", "firm", "product", "brand", "quantity", "price", "price_total","category", 'createds')

#     def get_product(self, obj):
#         products = Product.objects.filter(id=obj.product_id).values()
#         category_id= products[0]["category_id"]
#         return list(Product.objects.filter(id=category_id).values())[0]["name"]
        
#     def get_category(self,obj):
#         products = Product.objects.filter(id=obj.product_id).values()
#         # print(products)
#         category_id= products[0]["category_id"]
#         return list(Category.objects.filter(id=category_id).values())

#     def get_createds(self,obj):
#         products = Product.objects.filter(id=obj.product_id).values()
#         print(products)
#         purchase_id= products[0]["id"]
#         return list(Product.objects.filter(id=purchase_id).values())[0]["createds"]



# class SalesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sales
#         fields = ("id", 'user', 'product', 'brand', 'quantity', 'price', 'price_total')
#         # exclude = ('quantity',)