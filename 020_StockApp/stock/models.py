from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class UpdateCreate(models.Model):  # abstract base class ortak fieldleri burada tanımlıyoruz. abstract olduğunu class metada tanımlıyoruz.
    createds = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'

class Brand(models.Model):
    name = models.CharField(max_length=25, unique=True, blank=True)
    image = models.TextField()
    def __str__(self):
        return f'{self.name}'

class Product(UpdateCreate):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, max_length=25, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, max_length=25, on_delete=models.CASCADE, related_name='b_products')
    stock = models.PositiveSmallIntegerField(blank=True, default=0)
    createds = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.category}'

class Firm(UpdateCreate):
    name = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    image = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Purchases(UpdateCreate):
    user = models.ForeignKey(User, max_length=25, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, max_length=25, on_delete=models.SET_NULL, null=True, related_name="purchases")
    brand = models.ForeignKey(Brand, max_length=25, on_delete=models.SET_NULL, null=True, related_name="b_purchases")
    product = models.ForeignKey(Product, max_length=25, on_delete=models.CASCADE, related_name="purchase")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.product} - {self.quantity}'


class Sales(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="b_sales")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sale")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.product} - {self.quantity}'

 #?------------- blank=True , null=True ----------------
    # blank=True, serializer ile ilgilidir, yani boş bırakılabilir,
    # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
    #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
    #! bir işlem/hesaplama vs. yapılıp DB boş/null gitmesini önlemek gerekir.