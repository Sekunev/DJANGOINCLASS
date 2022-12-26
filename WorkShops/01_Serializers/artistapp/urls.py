from django.urls import path
from .views import (
    home,
    artist_api,
    album_api,
    song_api,
    # artist_detail,
    # artist_update,
    # artist_delete,
    artist_get_put_delete,
    SongLyric
    )

urlpatterns = [
    path('', home),
    path('artist/', artist_api),
    # path('artist-detail/<int:pk>/', artist_detail),
    # path('artist-delete/<int:pk>/', artist_delete),
    # path('artist-update/<int:pk>/', artist_update),
    path('artist/<int:pk>/', artist_get_put_delete),
    path('song-lyric/', SongLyric),

    path('album/', album_api),
    path('song/', song_api),
]