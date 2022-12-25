from django.urls import path
from .views import home, artist_api, album_api, song_api

urlpatterns = [
    path('', home),
    path('artist/', artist_api),
    path('album/', album_api),
    path('song/', song_api),
]