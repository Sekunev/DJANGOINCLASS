from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view()  
# api_view decoratördür. Ne işe yarar.Bir fonksiyondur.
# Arka planda GET, POST .. işlemlerini yapıyor.
# Response sayesinde JSON formatında veri elde etmeye yarıyor.
# Defaultu GET'dir.

def home(request):
    return Response({'home': 'This is home page...'})

# def home(request):
#     return HttpResponse({'home': 'This is home page...'})
# Yukardaki gibi tanımlasaydık. sadece key'i ekrana yazdıracaktı. Response ile yaptığımız için JSON döndü.
# daha önce (return HttpResponse('<h1>API Page</h1>')) HttpResponse ile return yaparken şimdi Response ile return yapıyoruz nedeni JSON döndürmek.
# dict içerisine key value şeklinde değerler yazdığımızda JSON'un temellerini atmıi oluyoruz.
# Aslında serializer'ında yaptığı tamda bu. queryset i alıyor ve jason a çeviriyor.

# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# ?(PUT yönteminde 1 field'de değişiklik yapacaksak olsak bile diğer field'leride göndermemiz gerekiyor.)
# - delete (dB de kayıt silme)
# - patch (kısmi update)
# ?(patch yönteminde 1 field'de değişiklik yapacaksaksak sadece o field'i göndermemiz yeterli. Reqired olan başka field'leri bu yöntemle girmesekde oluyor. )

#! /*** GET ***/

@api_view(['GET'])  # default GET
def student_list(request):
    students = Student.objects.all()  # Bütün öğrencileri çektim students'a atadım. Format <QuerySet [<Student: aa aaa>, <Student: s ss>]
    # print(students)
    serializer = StudentSerializer(students, many=True)  # Çektiğim verileri JSON'a çevirmek için valuesi StudentSerializer olan değişken (serializer) e atama yapıyorum. Birden çok obje çekeceksem many=True yazıyorum.
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

#! /*** POST ***/

@api_view(['POST'])  
def student_create(request):
    # Veri databaseden gelmeyecek o yüzden direkt gelen veriyi serializer yapıyoruz.
    # Frontend'den gönderilen dataya request.data şeklinde ulaşabiliyoruz.
    serializer = StudentSerializer(data=request.data)
    #? serializer edilmiş datanın valid olup olmadığını kontrol etmeliyiz. valid olması modelde belirtilen türlere uyup uymadığıdır.
    if serializer.is_valid():
        # valid ise kaydet
        serializer.save()
        message = {
            "message" : f"Student create Succesfully..."
        }
        # return Response(message) # ayrı bir mesaj'da yazdırabiliriz.
        # serializer.data dönmesi isteğe bağlı. Respons içerisine eklenirse kullanıcıya ne eklendi bunun bilgiside gelir. 
        # Genel olarak başarılı bir responsda HTTP_201_CREATE mesajı yazdırılır.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    # valid değilse serializer valid errorlarının dönmesini yani hangi field'de ne hatası var bunu döndürüyorum. aşağıda
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #! /*** DETAİL TEK OBJEYE YAPILAN İŞLEMLER  ***/

@api_view(['GET'])
def student_detail(request, pk):
    # pk : Çağırılan objenin id'si. Primary key.

    # student = Student.objects.get(id=pk)
    # Student tablosundaki id'si pk'ya eşit olan
    # Yukarıdaki yöntemi uyguladığımızda id'si olmayan bir sorgu yapıldığında hata alırız. Bunu önlemek için 2 yöntem var.
    # 1.si try except
    #! 2. get_object_or_404 yöntemi. Bu yöntem id'si x olanı çek yoksa 404 not found hatası ver demek oluyor.
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(student)
    # tek eleman olduğu için many=True yazmadık.
    return Response(serializer.data)

#! /*** PUT ***/

@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    # instance=student parametresi ile data'dan gelen gelenle kıyaslama yapıyor
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! /*** DELETE ***/

@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)


#############################################################
# Best Practice' Yukardaki gibi tek tek fonksiyon yazmak yerine id gerektiren ve gerektirmeyenler olmak üzere 2 fonksiyonla bu işlemleri yapabiliriz.

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)