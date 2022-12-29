from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet



@api_view()
def todo_home(request):
    return Response({'home': 'This is todo home page'})


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.filter(is_done=False) # Tamamlanmayanlar gelsin.
        serializer = TodoSerializer(todos, many=True)  # Queryset türünde ve 1'den çok veri geleceği için.
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'GET':
        # todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(data=request.data, instance=todo)
        # instance=todo bu parametreyi koymazsak yeni bir obje üretir. instance sayesinde karşılaştırma yapıyor. fark versa güncelliyor.
        # instance key'ini koymasaydık todo'yu başa yazmamız gerekirdi. Neden kwarg olduğu için yerinde olmalı.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'todo deleted succesfully'})

class Todos(ListCreateAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer
    lookup_field = 'id' # Eğer urls.py'da id tanımlamasını id yapmışsak burada lookup_field= 'id' olmalı. Defaul'u pk'dır.


class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer