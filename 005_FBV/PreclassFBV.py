# Şimdi fonksiyon tabanlı görünümleri kullanacağız . fscohort_api/ views .py dosyanızı açın ve bu kodu yazın.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from fscohort.models import Student


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all students, or create a new student.
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    """
    Retrieve, update or delete student.
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 1. satırda durum kodumuzu kullanmak için view'ımızı import ederek status modülünü yapıyoruz. Durum kodunun tam listesini burada görebilirsiniz
# https://www.django-rest-framework.org/api-guide/status-codes/

# 2. satırda , müşteri isteğine bağlı olarak birden çok içerik türüne dönüştürülebilen içeriği döndürmenize olanak tanıyan Response sınıfını içe aktardık.

# 3. satır api_view dekoratörünü içe aktarıyoruz. DFR'yi kullanmak için işlev tabanlı görünümler yazarken bunu kullanmalıyız.

# 15. satırda öğrenci nesnesini seri hale getirdik ve many=True kullandık. Birden fazla nesneyi seri hale getirdiğinizde many=True kullanmanız gerekir .

# 19. satır request.data kullandık . request.data , istek gövdesinin ayrıştırılmış içeriğini döndürür. Bu, request.POST standardına benzer . POST dışındaki HTTP yöntemlerinin içeriğinin ayrıştırılmasını destekler , yani PUT ve PATCH isteklerinin içeriğine erişebilirsiniz .

# Gördüğünüz gibi, Django işlev tabanlı görünümlere çok benzer . Şimdi URL'lerimizi yapılandırmamız gerekiyor.

# clarusway/urls.py dosyanızı açın ve bu URL'yi ekleyin.

urlpatterns = [
    ........
    path('api/', include('fscohort_api.urls'))
]

# fscohort_api/urls.py dosyanızı açın

from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list),
    path('< int:pk >/', views.student_detail),
]

http://127.0.0.1:8000/api/ adresine gittiğinizde django rest çerçevesinden göz atılabilir bir api görebilirsiniz .

