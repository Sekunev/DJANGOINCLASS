from .views import home, artist_api

urlpatterns = [
    path('', home),
    path('artist/', artist_api),
]