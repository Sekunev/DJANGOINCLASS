from django.urls import path, include
from rest_framework import routers

from .views import (
    #! FOR FUNCTION 
    home,
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
    # student_api,
    # student_api_get_update_delete,
    #! FOR CLASS BASED 
    # StudentListCreate,
    # StudentDetail,
    #! FOR GENERIC
    # StudentGAV,
    # StudentDetailGAV
    #! FOR CONCRETE
    # StudentCV,
    # StudentDetailCV,
    #! FOR VIEWSET
    StudentMVS,
    PathMVS
)

#? VIEWSET yöntemi ile tanımlama yapıldığında urls.py'de router tanımlaması yapılması gerekli.
#? path kısmında'da router'ı çağırıyoruz.
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
# dökumandaki prefix--> student.
# dökumandaki url_path--> primarykey.


router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)

urlpatterns = [
    #! FOR FUNCTION 
    path("", home),
    # path("student-list/", students_list, name='list'),
    # path("student-create/", student_create, name='create'),
    # path("student-detail/<int:pk>/", student_detail, name='detail'),
    # path("student-update/<int:pk>/", student_update, name='update'),
    # path("student-delete/<int:pk>/", student_delete, name='delete'),
    #! Birleşmiş hali.
    # path('student', student_api),
    # path('student/<int:pk>', student_api_get_update_delete)

    #! FOR CLASS BASED  .as_view() keywordu gerekli.
    # path('student/', StudentListCreate.as_view()),
    # path('student/<int:pk>', StudentDetail.as_view())
    #! FOR GENERIC
    # path('student/', StudentGAV.as_view()),
    # path('student/<int:pk>', StudentDetailGAV.as_view())
    #! FOR CONCRETE
    # path('student/', StudentCV.as_view()),
    # path('student/<int:pk>', StudentDetailCV.as_view())
    #! FOR VIEWSET
    path('', include(router.urls)),

]

# urlpatterns += router.urls --> router bu şekilde de eklenebilir.