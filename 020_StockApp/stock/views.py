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

class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']

class PurchaseView(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['firm', 'product']
    search_fields = ['firm']    
    # Bir Purchases ceate edildiğinde Product/stok miktarının otomatik artması için.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #! #############  ADD Product Stock ############
        
        purchase = request.data
        product = Product.objects.get(id=purchase["product_id"])
        product.stock += purchase["quantity"]
        product.save()
        
        #! #############################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # serializer.save()   # Bu Purchases'i kim create ediyorsa onu user fieldinden basitçe almak için save metoduna parametre olarak ekliyoruz.      
        serializer.save(user=self.request.user)         
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        #! #############  UPDATE Product Stock ############
        
        purchase = request.data
        product = Product.objects.get(id=instance.product_id)
        
        # eski quantity - yeni quantity stok miktarına ekleyerek stok'u güncellemiş oluyoruz.
        sonuc = purchase["quantity"] - instance.quantity  
        product.stock += sonuc
        product.save()
        
        #! #############################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
         #! #############  DELETE Product Stock ############       
        product = Product.objects.get(id=instance.product_id)
        product.stock -= instance.quantity
        product.save()
        #! #############################################
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class SalesView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand','product']
    search_fields = ['brand']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #! #############  REDUCE Product Stock ############
        # Purchases'deki create işleminden farklı olarak Burada product.stock'daki miktar kontrol edilmeli, Yeterli stock varsa sales işlemi gerçekleşmeli. Yoksa yeterli stok olmadığı kullanıcıya bir mesaj ile bildirilmeli.
        sales = request.data
        product = Product.objects.get(id=sales["product_id"])
        
        if sales["quantity"] <= product.stock:
            product.stock -= sales["quantity"]
            product.save()
        else:
            data = {
                "message": f"Dont have enough stock, current stock is {product.stock}"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        #! #############################################
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        #!####### UPDATE Product Stock ########
        sale = request.data
        product= Product.objects.get(id=instance.product_id) 
        print(product.stock)
        print(instance.quantity)
        # Aşağıda ne yaptık: 
        # ilk Koşul: put ile gönderilen Güncellenecek miktar(sale["quantity"]) daha önce post ile oluşturulan (instance.quantity) quantity'den büyükmü
        # Büyükse post ile oluşturulan (instance.quantity) ve product.stock toplamındanda büyükse product.stock ve instance.quantity toplamından sale["quantity"]'yi çıkarıyoruz.
        #  sale["quantity"] --> instance.quantity + product.stock küçükse Satış yapmak için yeterli stok bulunmadığı uyarısını kullanıcıya veriyoruz.
        # 2. Koşul elif ilede post ile oluşturulan (instance.quantity) post ile oluşturulan (instance.quantity) den küçük eşit ise instance.quantity dan sale["quantity"] in çıkarılmış halini product.stock'a eşitleyerek logic'i oluşturuyouz.
        if sale["quantity"] > instance.quantity:
            
            if sale["quantity"] <= instance.quantity + product.stock:
                product.stock = instance.quantity + product.stock - sale["quantity"]
                product.save()
            else:
                data = {
                "message": f"Dont have enough stock, current stock is {product.stock}"
                }
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        # mevcut yeniden büyük eşitse
        elif sale["quantity"]  <= instance.quantity  :
            product.stock += instance.quantity - sale["quantity"]
            product.save()
         
        #!##################################
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # sales silindiğinde belirtilen sales'deki miktarın product.stock'a eklenmesi için 
        #!####### DELETE Product Stock ########
        product = Product.objects.get(id=instance.product_id)
        product.stock += instance.quantity
        product.save()
        #!##################################
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)