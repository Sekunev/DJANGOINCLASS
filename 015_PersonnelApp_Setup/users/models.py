from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date
from django.contrib.auth.models import User

# Create your models here.
#! Daha karmaşık user modeli oluşturmak istersek bunu 2 yolu bulunuyor.
#? 1
# User modeli --> class User(AbstractUser): inherit edilerek yapılmış
# Biz de AbstractUser'dan  inherit ederek kendi User modelimizi oluşturabiliriz.
# Buna exdending user table deniyor,
# Buna aşağıdaki myUser modelini örnek olarak verebiliriz.
# Bu yöntem için admin.py a eklemeler yapmalıyız. 
# aynı zamanda base.py'a da # AUTH_USER_MODEL = 'users.MyUser' kodunu eklemeliyiz



# class MyUser(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'  # Bu şekilde olduğunda superuser olarak email baz alınmış olacak.
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
#   def __str__(self):
#       return "{}".format(self.email)

#? 2
# yeni bir tablo oluşturup, bunu onetoone ile mevcut User tablosuna bağlayarak yapma;
# böylece mevcut User'lara ilave fieldlar ekleyebiliriz.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # her user'in 1 tane profili olacak.'
    display_name = models.CharField(max_length=30, blank = True, null = True)
    avatar = models.ImageField(upload_to="pictures", default = 'avatar.png')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile'"