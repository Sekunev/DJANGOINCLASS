from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions # https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions

# Create your views here.
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]  # filtre ve search işlemi için sadece 
    search_fields = ['name']  # import edip view içerisine bu iki satır kodu yazmamız yeterli oldu.
    filterset_fields = ['name']
    permission_classes=[DjangoModelPermissions]  # Userlar ile gruplar oluşturup Hangi user'in hangi grupta olduğunu belirleyerek permission belirlemek için. Bu tanımlamayı yaptıktan sonra gruba dahil edilen user'ın token i ile auth olarak istek yapılabilir.

# query params name ise CategoryProductSerializer'ın çalışması için. değilse 'CategorySerializer çalışması için.
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductSerializer
        return super().get_serializer_class()



# class BrandView(ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class ProductView(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class FirmView(ModelViewSet):
#     queryset = Firm.objects.all()
#     serializer_class = FirmSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter

# class PurchasesView(ModelViewSet):
#     queryset = Purchases.objects.all()
#     serializer_class = PurchasesSerializer

#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['firm']
#     search_fields = ['firm__name']
#     ordering_fields = ['id']
#     ordering = ['-id'] 



#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         quantity_ = serializer.validated_data.get('quantity')
#         price_ = serializer.validated_data.get('price')
#         response.data['price_total'] = quantity_ * price_

#         return response 

# class SalesView(ModelViewSet):
#     queryset = Sales.objects.all()
#     serializer_class = SalesSerializer

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         quantity_ = serializer.validated_data.get('quantity')
#         price_ = serializer.validated_data.get('price')
#         response.data['price_total'] = quantity_ * price_

#         return response 