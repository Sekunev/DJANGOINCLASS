from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

class PurchasesView(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer

    def create(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # purchase = serializer.save()
        # purchase.price_total = purchase.quantity * purchase.price
        # purchase.save()

        quantity_ = serializer.validated_data.get('quantity')
        price_ = serializer.validated_data.get('price')
        price_total_ = serializer.validated_data.get('price_total') 
        price_total_ = quantity_ * price_

        price_total_.save() 

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SalesView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer