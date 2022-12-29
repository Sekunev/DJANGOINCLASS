from django.urls import path, include
from rest_framework import routers
from .views import (
    todo_list_create,
    todo_home,
    todo_detail,
    Todos,
    TodoDetail,
    TodoMVS
)

router = routers.DefaultRouter()
# todo/ todo/path  todo/<int:pk>  todo/<int:pk>/path
router.register('todo', TodoMVS)

urlpatterns = [
    # path('', todo_home),
    #! Function view
    # path('list-create/', todo_list_create),
    # path('detail/<int:id>', todo_detail),
    #! class view
    # path('list-create/', Todos.as_view()),
    # path('detail/<int:id>', TodoDetail.as_view()),
    #! MVS
    path('', include(router.urls))
    # veya urlpatterns += router.urls
]
