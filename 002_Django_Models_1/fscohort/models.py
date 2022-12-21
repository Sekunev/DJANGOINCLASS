from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(default=1111)
    about = models.TextField(blank=True, null=True) #? null=True boş bırakılabilir.(null yazar) blank=True --> boş bırakılabilir.
    register = models.DateTimeField(auto_now_add=True) #? auto_now_add: Take the creation data and time
    last_updated_date = models.DateTimeField(auto_now=True) #? auto_now: Take the update data and time
    is_active = models.BooleanField()

#! aşağıdaki metot database'de değişiklik yapmadığı için migrate yapmaya gerek yok
# Aşağıdaki metod objelerin görünümünü ayarlıyor.

    def __str__(self):
        return f"{self.number} {self.first_name}  {self.last_name} "
#? class Meta ile Student clasının bazı özelliklerini ayarlayabiliyoruz. 
# https://docs.djangoproject.com/en/4.1/topics/db/models/#model-methods

    class Meta:
        ordering = ["number"] # numaraya göre sıralama
        verbose_name_plural = "Student_List" # adminpanel'deki class ismini değiştiriyor.

    def student_year_status(self):
        "Returns the student's year status"
        import datetime
        if self.register < datetime.date(2019, 1, 1):
            return "Senior"
        if self.register < datetime.date(2021, 1, 1):
            return "Junior"
        else:
            return "Freshman"
