from django.urls import path, include
from rest_framework import routers
from .views import (
    home,
    artist_api,
    album_api,
    song_api,
    # artist_detail,
    # artist_update,
    # artist_delete,
    # artist_get_put_delete,
    #! CLASS BASED VIEWS
    # ArtistListCreate,
    # ArtistDetail,
    # !GENERIC API VIEWS and Mixins
    # ArtistGAV,
    # StudentDetailGAV
    # !CONCRETE VIEWS 
    ArtistCV,
    ArtistDetailCV,
    #! VIEWSET
    ArtistMVS,
    AlbumMVS
    )

router = routers.DefaultRouter()
router.register("artist", ArtistMVS)
router.register("album", AlbumMVS)

urlpatterns = [
    path('', home),
    # path('artist/', artist_api),
    # path('artist-detail/<int:pk>/', artist_detail),
    # path('artist-delete/<int:pk>/', artist_delete),
    # path('artist-update/<int:pk>/', artist_update),
    # path('artist/<int:pk>/', artist_get_put_delete),
    #! CLASS BASED VIEWS
    # path('artist/', ArtistListCreate.as_view()),
    # path('artist/<int:pk>', ArtistDetail.as_view()),
    # !GENERIC API VIEWS and Mixins
    # path('artist/', ArtistGAV.as_view()),
    # path('artist/<int:pk>', StudentDetailGAV.as_view()),
    #! CONCRETE VIEWS 
    # path('artist/', ArtistCV.as_view()),
    # path('artist/<int:pk>', ArtistDetailCV.as_view()),
    #! FOR VIEWSET
    path('', include(router.urls)),

    # path('album/', album_api),
    # path('song/', song_api),
]