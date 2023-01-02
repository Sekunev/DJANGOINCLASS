from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

# https://www.django-rest-framework.org/api-guide/validators/#validators
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())]) # email uniq ve standartlara uygun olmasını sağlıyoruz.
    password = serializers.CharField(write_only=True)  # defaultunda required=True  olduğu için eklemedik.
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'

        )
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password' : 'Password fields didnt match'}
            )
        
        return attrs

    def create(self, validated_data):
        #print(validated_data) #? {'username': 'Cooper', 'email': 'a@a.com', 'first_name': 'Co', 'last_name': 'Per', 'password': '1234566Aa.', 'password2': '123456Aa.'}
        validated_data.pop('password2') #? {'username': 'Cooper', 'email': 'a@a.com', 'first_name': 'Co', 'last_name': 'Per', 'password': '1234566Aa.'}
        password = validated_data.pop('password') #? {'username': 'Cooper', 'email': 'a@a.com', 'first_name': 'Co', 'last_name': 'Per'}
        user = User.objects.create(**validated_data) #? {'username': 'Cooper', 'email': 'a@a.com', 'first_name': 'Co', 'last_name': 'Per'}
        user.set_password(password) #? password'un encrypte olarak db ye kaydedilmesini sağlıyor.
        user.save()
        return  user


    

        