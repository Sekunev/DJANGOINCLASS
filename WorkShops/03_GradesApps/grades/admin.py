from django.contrib import admin
from .models import Teacher,Lessons, Students, Grade

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Lessons)
admin.site.register(Students)
admin.site.register(Grade)