
from django.urls import path, include
from .views import LessonsMVS, StudentsMVS, GradeMVS, TeacherMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacher', TeacherMVS)
router.register('students', StudentsMVS)
router.register('grade', GradeMVS)
router.register('lessons', LessonsMVS)

urlpatterns = router.urls