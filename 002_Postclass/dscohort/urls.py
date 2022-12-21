from django.urls import path
from .views import preclass



urlpatterns = [
    path('', preclass),

]