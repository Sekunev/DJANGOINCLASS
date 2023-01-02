from django.shortcuts import render
from .serializer import PostSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Post, Category

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission



# Create your views here.
class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        else:
            return request.user.is_staff

    #! Concrete
class CategoryListCV(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]  #* admin olan herkes CRUD yapabilir. Olmayan sadece get yapabilir.

    filterset_fields = ['name']
    search_fields = ['^name']
    ordering_fields = ['id']

class CategoryDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    #! ModelViewSet
class PostMVS(ModelViewSet):
    filterset_fields = ['category']
    search_fields = ['^title']
    ordering_fields = ['id']
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly] #* Authenticat olan herşeyi yapar, olmayan (sadece) GET(read) yapar.





