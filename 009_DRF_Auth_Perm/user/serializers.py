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
    first_name = serializers.CharField(required=True)
# write_only = True --> Bu Field'i sadece Post veya Put yaparken kullan. Sonrasında gösterme.
# read_only = True  --> Create işlemlerinde değil get işlemlerinde kullan-göster.

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
    # password ile password2 aynımı bunun validasyonunu yapmamız gerekiyor. Bunun için validate (override) metodu kullanılıyor.
    def validate(self, data): # data yujkardaki field içerisindeki attributler. 
        #print(data)  # OrderedDict([('username', 'aaa'), ('email', 'aa@a.com'), ('first_name', 'aa'), ('last_name', 'aaa'), ('password', '123456Aa'), ('password2', '123456Aa.')])
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                # hata mesajı oluştur.
                {'password': 'Password fields didnt match'  }
            )
        return data

    def create(self, validated_data):
        print(validated_data)  # {'username': 'fffs', 'email': 'fffd@s.com', 'first_name': 'aa', 'last_name': 'aaa', 'password': 'aa111122a', 'password2': 'aa111122a'}
        validated_data.pop('password2') # validated_data'dan password2'yi sil.
        password = validated_data.pop('password')  # validated_data'dan password'i sil password'e ata.
        user = User.objects.create(**validated_data) #unpack --> alternatif yazım --> username=validated_data['username'], email = vali....
        # user artık validated_data'nın password'ler olmayan hali.
        user.set_password(password)  # password'un encrypte olarak db ye kaydedilmesini sağlıyor. 
        user.save()
        return user
