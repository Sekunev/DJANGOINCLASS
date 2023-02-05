from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('categories', CategoryView)
router.register('brands', BrandView)
router.register('firm', FirmView)
router.register("products", ProductView)
router.register('purchases', PurchaseView)
router.register('sales', SalesView)

urlpatterns = router.urls
