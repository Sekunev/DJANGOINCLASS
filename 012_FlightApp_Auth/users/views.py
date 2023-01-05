from rest_framework.generics import CreateAPIView
# CreateAPIView : Yeni bir model örneği oluşturmak için HTTP POST isteklerini işler.
from django.contrib.auth.models import User # Model yazmadık hazır user modeli import ettik.
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

    # Register olunduğunda response ile birlikte token'inde dönerek login sayfasına gitmeden direk auth olabilmek için: OOP'den hatırlayalım bir metod kendi içerisinde varsa parent'e gitmez.
    # generic/mixins'den override yapıyoruz. respose'a token'i de dahil ediyoruz. importları parentdan aldık.
class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user) # Token Tablosundan tokeni aldım.
        data = serializer.data
        data["token"] = token.key # data'ya token elemanı ekledik.
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)