from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    bio = models.TextField(max_length=200)
    register_date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"({self.id} {self.username} {self.age})"
        
    class Meta:
        ordering = ('username',)
        verbose_name = "Profil"

#! auto_now : Nesne her kaydedildiğinde alanı otomatik olarak şimdi olarak ayarlar.

#! auto_now_add : Nesne ilk oluşturulduğunda alanı otomatik olarak şimdi olarak ayarlayın.