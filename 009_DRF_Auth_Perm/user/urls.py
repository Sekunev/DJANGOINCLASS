from django.urls import path
from .views import RegisterView, logout
from rest_framework.authtoken import views

#  obtain_auth_token: DB'e token olup olmadığını kontrol ediyor. token varsa Response olarak varolan token dönüyor. Yoksa oluşturup response ediyor.

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', logout),

]