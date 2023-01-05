from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ogretmen"
        
class Lessons(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dersler"

class Students(models.Model):
    number = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "ogrenci"

class Grade(models.Model):
    student = models.ManyToManyField(Students)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return self.grade

    class Meta:
        verbose_name = "not"
