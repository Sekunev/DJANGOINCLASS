from django.shortcuts import render
from .serializer import PostSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Post, Category


# Create your views here.
    #! Concrete
class CategoryListCV(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    search_fields = ['^name']
    ordering_fields = ['id']

class CategoryDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #! ModelViewSet
class PostMVS(ModelViewSet):
    filterset_fields = ['category']
    search_fields = ['^title']
    ordering_fields = ['id']
    queryset = Post.objects.all()
    serializer_class = PostSerializer

