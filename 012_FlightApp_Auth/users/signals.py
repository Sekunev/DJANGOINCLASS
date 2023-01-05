from django.contrib.auth.admin import User
from django.db.models.signals import post_save
# post save edilir edilmez sinyal göndermesi için post_save
from django.dispatch import receiver
# receiver ile sinyalı yakalıyoruz.
from rest_framework.authtoken.models import Token
# Tokeni create edeceğimiz Token Tablosu.
# https://www.django-rest-framework.org/api-guide/authentication/
# Aşağıdaki işlemle User tablomda bir kullanıcı oluştuğu zaman Sİnyali yakalayıp Token tablosunda da Token oluşturuyoruz.
@receiver(post_save, sender=User) # gönderen User Tablosu.
# create_Token'ı yukarıdaki kaydetme ve yakalama işlemi tetikliyor. 
def create_Token(sender, instance=None, created=False, **kwargs ): # instance User'ın gönderdiği sinyal. User Create edildikten sonra created True dönüyor.
    if created:
        Token.objects.create(user=instance) # user'i sinyali gönderen user'a atadık.
        