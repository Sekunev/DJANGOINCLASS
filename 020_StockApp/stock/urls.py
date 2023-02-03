from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('categories', CategoryView)
# router.register('brand', BrandView)
# router.register('product', ProductView)
# router.register('firm', FirmView)
# router.register('purchases', PurchasesView)
# router.register('sales', SalesView)

urlpatterns = router.urls
