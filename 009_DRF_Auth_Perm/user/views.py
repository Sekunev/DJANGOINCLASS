from .serializers import RegisterSerializer
from django.contrib.auth.models import User # Model yazmadık hazır user modeli import ettik. 
from rest_framework.generics import CreateAPIView
# CreateAPIView : Yeni bir model örneği oluşturmak için HTTP POST isteklerini işler.
from rest_framework.authtoken.models import Token

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # Register olunduğunda response ile birlikte token'inde dönerek login sayfasına gitmeden direk auth olabilmek için:
    # generic/mixins'den override yapıyoruz. respose'a token'i de dahil ediyoruz.
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # print(response.data) # {'id': 9, 'username': 'sssaaaaa', 'email': 'sssaakaa@s.com', 'first_name': 'aa', 'last_name': 'aaa'}
        token = Token.objects.create(user_id = response.data["id"]) # database'de kullanıcı id'si user_id şeklinde kayıtlı olduğu için.
        response.data['token'] = token.key # response.data'ya tken elemanı ekledik.
        # print(response.data) # {'id': 10, 'username': 'sssaaaaaa', 'email': 'sssaakaaa@s.com', 'first_name': 'aa', 'last_name': 'aaa', 'token': 'd372d717c1383f2fade25a923c659ce7e60b9c4c'}
        # return response

# ! Override: bir classın bir alt sınıfındaki bir yöntem tanımında kullanılır ve bu yöntemin bir üst sınıfındaki aynı adlı yöntemi geçersiz kılma amacıyla tasarlandığını gösterir. 
# Aşağıda create metodunun override edilmemiş hali bulunuyor.
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
