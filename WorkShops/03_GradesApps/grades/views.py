from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .serializers import TeacherSerializer, LessonsSerializer, StudentsSerializer, GradeSerializer
from .models import Teacher, Students, Lessons, Grade
# Create your views here.

class TeacherMVS(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class LessonsMVS(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
class StudentsMVS(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
class GradeMVS(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


