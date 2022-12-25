from django.urls import path
from .views import (
    home, 
    student_list, 
    student_create,
    student_detail,
    student_update,
    student_delete,
    student_api,
    student_api_get_update_delete
    )

urlpatterns = [
    path("", home),
    # path("student-list/", student_list, name='list'),
    # path("student-create/", student_create, name='create'),
    # # pk: Primary Key
    # path("student-detail/<int:pk>", student_detail, name='detail'),
    # path("student-update/<int:pk>", student_update, name='detail'),
    # path("student-delete/<int:pk>", student_delete, name='detail'),
    path("student/", student_api, name='detail'),
    path("student/<int:pk>", student_api_get_update_delete, name='detail'),
]
