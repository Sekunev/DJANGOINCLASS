from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Purchases, Sales


@receiver(post_save, sender=Purchases)
def update_stock_purchases(sender, instance, created, **kwargs):
    if created:
        print('signal çalıştı', instance.product.stock)
        instance.product.stock += instance.quantity
        instance.product.save()
        print('signal çalıştı2', instance.product.stock)

@receiver(post_save, sender=Sales)
def update_stock_sales(sender, instance, created, **kwargs):
    if created:
        instance.product.stock -= instance.quantity
        instance.product.save()

# @receiver(post_save, sender=Purchases)
# def update_stock_purchases(sender, instance, **kwargs):
#     print('signal çalıştı', instance.product.stock)
#     instance.product.stock += instance.quantity
#     instance.product.save()
#     print('signal çalıştı2', instance.product.stock)

# @receiver(post_save, sender=Sales)
# def update_stock_sales(sender, instance, **kwargs):
#     instance.product.stock -= instance.quantity
#     instance.product.save()

