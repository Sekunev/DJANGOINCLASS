from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from .permissions import IsAdminOrReadOnly

class CategoryView(ModelViewSet):  # crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]  #* Admin olan herşeyi yapar, olmayan (sadece) GET(read) yapar.
    filterset_fields = ['name']


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  #* Authenticat olan herşeyi yapar, olmayan (sadece) GET(read) yapar.
    filterset_fields = ['category']
    # filterset_fields = ['category__name'] #? Filtrelemeyi id'ye göre değilde isme göre yapmak istersek.
    search_fields = ['title', 'content']
