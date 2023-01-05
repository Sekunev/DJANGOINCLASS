from rest_framework import serializers
from django.contrib.auth.models import User # Model yazmadık hazır user modeli import ettik. 
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from dj_rest_auth.serializers import TokenSerializer

#! email zorunlu ve uniq olsun istiyoruz.
# https://www.django-rest-framework.org/api-guide/validators/#validators
# validator kodunu link'den aldık.

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
  # email default required değil, onu değiştirdik, artık zorunlu alan
  # email uniq olsun, değilse validation error dönsün onun için ekledik ve yukarıda import ettik (UniqueValidator)
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password], # Base'deki validasyonlara uygun olsun.
        style = {"input_type" : "password"} # İnput girişi esnasında noktaların belirmesini sağlıyor.
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type" : "password"}
    )

    #? write_only sadece POST, PUT için kullan, GET(yani read) yapılırsa kullanma
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2'] # Bu field'ler import ettiğimiz modelde (sourcecode)bulunmaktadır.
    # password ile password2 aynımı bunun validasyonunu yapmamız gerekiyor. Bunun için validate (override) metodu kullanılıyor.

    def validate(self, data):# data yujkardaki field içerisindeki attributler. 
        #print(data)  # OrderedDict([('username', 'aaa'), ('email', 'aa@a.com'), ('first_name', 'aa'), ('last_name', 'aaa'), ('password', '123456Aa'), ('password2', '123456Aa.')])
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                # hata mesajı oluştur.
                {"message" : "Password fields didnt match!"}
            )
        return data

    #? ModelSerializer kullanınca create metodu yazmaya gerek yok aslında fakat, User model içinde olmayan bir field 
    #? (password2) kullandığımız için creat metodunu override etmek gerekli aynı zamanda password'u hash'leyerek kaydedeceğiz.;

    def create(self, validated_data):
        print(validated_data)  # {'username': 'fffs', 'email': 'fffd@s.com', 'first_name': 'aa', 'last_name': 'aaa', 'password': 'aa111122a', 'password2': 'aa111122a'}
        password = validated_data.get("password")
        # validated_data'dan password'i getir..
        validated_data.pop("password2")
        # validated_data'dan password2'yi sil.
        user = User.objects.create(**validated_data)
        #unpack --> alternatif yazım --> username=validated_data['username'], email = vali....
        # user artık validated_data'nın password2 olmayan hali.
        user.set_password(password)
        # password'un encrypte olarak db ye kaydedilmesini sağlıyor. 
        user.save()
        return user

# Aşağıdaki iki class'ı token ile birlikte kullanıcının diğer bilgilerininde  login olunduğunda döndürülmesi için yapıyoruz.
class UserTokenSerializer(TokenSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")

class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")