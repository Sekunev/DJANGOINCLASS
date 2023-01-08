from django.urls import path
from .views import FlightView, ReservationView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("flights", FlightView, basename='flights')  # basename amacı : flights ilerde değişsede tüm urls.py'lerden ayrı ayrı değiştirmeye gerek yok.
router.register("reservations", ReservationView)

urlpatterns = [
    
]
urlpatterns += router.urls