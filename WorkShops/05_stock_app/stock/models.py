from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'

class Brand(models.Model):
    name = models.CharField(max_length=25)
    image = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, max_length=25, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, max_length=25, on_delete=models.CASCADE)
    stock = models.SmallIntegerField()
    createds = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.category}'

class Firm(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Purchases(models.Model):
    user = models.ForeignKey(User, max_length=25, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, max_length=25, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, max_length=25, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, max_length=25, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    price_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.firm} - {self.product}'

    class Meta:
        # verbose_name = "Sales"
        verbose_name_plural = "Purchases"

class Sales(models.Model):
    user = models.ForeignKey(User, max_length=25, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, max_length=25, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, max_length=25, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    price_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.user} - {self.brand} - {self.product}'

    class Meta:
        # verbose_name = "Sales"
        verbose_name_plural = "Sales"
