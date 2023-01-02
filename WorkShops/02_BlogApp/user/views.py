from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):  #? owerride
        response =  super().create(request, *args, **kwargs)
        #print(response) #? HTTP response --> <Response status_code=201, "text/html; charset=utf-8">
        #print(response.data) #? {'id': 7, 'username': 'Muratab', 'email': 'aaaab@a.com', 'first_name': 'aaa', 'last_name': 'sss'}
        token = Token.objects.create(user_id = response.data['id'])

        response.data['token'] = token.key
        #print(response.data) #? {'id': 9, 'username': 'Muratabds', 'email': 'aaaabds@a.com', 'first_name': 'aaa', 'last_name': 'sss', 'token': '6c86f7e1dcda4c8570badab0dc5ac9d614641fa2'}
        return response

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})


