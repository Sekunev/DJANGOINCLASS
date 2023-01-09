from rest_framework import serializers
from .models import (Teacher, Students, Grade, Lessons)

class GradeSerializer(serializers.ModelSerializer):
  student = serializers.StringRelatedField()
  lesson = serializers.StringRelatedField()
  class Meta:
    model = Grade
    fields = ("student", "lesson", "grade")
            # serializer da uniquelik sağlamak için aşağıdaki metodu kullanıyoruz.Bu metotla admin panelde kısıtlama yapmış olmuyoruz. Burada yaptığımız işlem UniqueTogetherValidatorü import edip içine birleştiğinde unique olmasını istediğimiz fieldları veriyoruz ve kontrol etmesini istediğimiz queryseti veriyoruz o bizim yerimize kontrolü sağlıyor.Örneğimizde lesson ve student eşleşmeleri böylelikle istediğimiz gibi tek olmuş oluyor. Aynı isimde ders birden fazla öğrenci ile eşleşebilir ama aynı öğrenci ile eşleşemez aynı şekilde öğrenci için de öyle.
    # validators = [
    #     UniqueTogetherValidator(
    #         queryset=Grade.objects.all(),
    #         fields=['lesson_id', 'student_id']#create işleminde kullanılan fieldları yazıyoruz
    #     )
    # ]
    
  

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ("id", "name")
    
    
class LessonsSerializer(serializers.ModelSerializer):
  lesson_grades = GradeSerializer(many=True)
  class Meta:
    model = Lessons
    fields = ("id", "name", "teacher", "lesson_grades")
    
    
class StudentsSerializer(serializers.ModelSerializer):
  student_grades = GradeSerializer(many=True)
  class Meta:
    model = Students
    fields = ("number", "first_name", "last_name", "student_grades")


