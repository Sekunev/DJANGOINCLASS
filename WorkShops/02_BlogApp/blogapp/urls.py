from django.urls import path, include
from .views import CategoryListCV, CategoryDetailCV, PostMVS
from rest_framework import routers

#! ModelViewSet
router = routers.DefaultRouter()
router.register("post", PostMVS)

urlpatterns = [
    #! Concrete
    path('category/', CategoryListCV.as_view()),
    path('category/<int:pk>', CategoryDetailCV.as_view()),
    #! ModelViewSet
    path('', include(router.urls))
]
    #! Alternatif ModelViewSet
urlpatterns += router.urls