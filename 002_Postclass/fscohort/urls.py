from django.urls import path
from .views import postclass, postclass1



urlpatterns = [
    path('', postclass),
    path('postclass1', postclass1),

]