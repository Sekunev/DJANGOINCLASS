from django.db import models

# Create your models here.
class Student(models.Model):
first_name = models.CharField(max_length=50)
last_name = models.CharField(max_length=50)
number = models.IntegerField()
about = models.TextField(blank=True, null=True)
register = models.DateTimeField(auto_now_add=True) #? auto_now_add: Take the creation data and time
last_updated_date = models.DateTimeField(auto_now=True) #? auto_now: Take the update data and time
is_active = models.BooleanField()