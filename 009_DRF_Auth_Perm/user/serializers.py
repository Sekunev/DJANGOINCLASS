from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User # Model yazmadık hazır user modeli import ettik. 

#! email zorunlu ve uniq olsun istiyoruz.
# https://www.django-rest-framework.org/api-guide/validators/#validators
# validator kodunu link'den aldık.
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True) # password'ün doğru girilip girilmediğini kontrol eden field.

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
        )  # Bu field'ler import ettiğimiz modelde (sourcecode)bulunmaktadır.

# write_only = True --> Bu Field'i sadece Post veya Put yaparken kullan.
# read_only = True  --> Create işlemlerinde değil get işlemlerinde kullan.