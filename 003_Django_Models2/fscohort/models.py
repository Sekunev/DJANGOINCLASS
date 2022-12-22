from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    #? blank: bos alan olup olamama durumu true yazmazsan boş bırakamazsın uyarı verir. null: null degeri alip alamama durumu
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='student')
    register_date = models.DateTimeField(null=True, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"({self.number}-{self.first_name} {self.last_name})"

    class Meta:
        ordering= ('-number',)
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        db_table= "" # Tablo ismini değiştir.