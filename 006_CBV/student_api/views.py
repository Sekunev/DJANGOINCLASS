from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# my imports
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer

#! VIEW TANIMLAMANIN 5 YOLU.
#! 1- FUNCTION BASED VIEWS.
#! 2- CLASS BASED VIEWS.
#! 3- GENERIC API VIEWS and Mixins
#! 4- CONCRETE VIEWS 
#! 5- VIEWSET




#* #################### 
#! 1- FUNCTION BASED VIEWS 
#* ####################

@api_view()  # default GET
def home(requst):
    return Response({'home': 'This is home page...'})


# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# - delete (dB de kayıt silme)
# - patch (kısmi update)

#***! sadece  ['GET'] ***/
@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    # print(students)
    serializer = StudentSerializer(students, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

#***! sadece  ['POST'] ***/
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student created succesfully....'
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#***! id eklenerek Tek elemanlı   ['GET'] ***/
@api_view(['GET'])
def student_detail(request, pk):

    student = get_object_or_404(Student, id=pk)
    # student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

#***! id eklenerek Tek elemanlı   ['PUT'] ***/
@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#***! id eklenerek Tek elemanlı   ['DELETE'] ***/
@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)


#***! Birleştirilmiş   ['GET', 'POST'] ***/

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

#***! Birleştirilmiş id eklenerek Tek elemanlı ['GET', 'PUT', 'DELETE', 'PATCH'] ***/
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


#* #################### 
#! 2- CLASS BASED VIEWS 
#* ####################

#***! Tek Class içerisinde ['GET', 'POST'] ***/
# APIView'i import et.
# https://www.django-rest-framework.org/api-guide/views/
class StudentListCreate(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#***! Tek Class içerisinde ['GET', 'PUT', 'DELETE'] ***/

class StudentDetail(APIView):
    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)
    
    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)


#* #################### 
#! 3- GENERIC API VIEWS and Mixins
#* ####################

# https://www.django-rest-framework.org/api-guide/generic-views/

""" #? GenericApıView 
# One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

# GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

#? Mixins
#* Mixins Belli görevi yapmak için oluşturulmuş classlardeı. Kendi başına çalışamaz. Çalışması için başka yapıya ihtiyaç duyar.
# - ListModelMixin
#     - list method
# - CreateModelMixin
#     - create method
# - RetrieveModelMixin
#     - retrieve method
# - UpdateModelMixin
#     - update method
# - DestroyModelMixin
#     - destroy method 
    

class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) """

#***! Tek Class içerisinde ['GET', 'POST'] ***/
# ListModelMixin -->  öğrencileri çağırmaya yarar.
# CreateModelMixin -->  öğrencileri oluşturmaya yarar.
# GenericAPIView --> Yokardaki fonksiyonları çalıştırmaya yarar.

class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)

    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)

#***! Tek Class içerisinde ['GET', 'PUT', 'DELETE'] ***/
# RetrieveModelMixin --> Tek öğrenciyi çağırmaya yarar.
# UpdateModelMixin --> Tek öğrenciyi updateye yarar.
# DestroyModelMixin --> Tek öğrenciyi silmeye yarar.
# GenericAPIView --> Yokardaki fonksiyonları çalıştırmaya yarar.

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *arg, **kwargs):
        return self.retrieve(request, *arg, **kwargs)

    def put(self, request, *arg, **kwargs):
        return self.update(request, *arg, **kwargs)

    def delete(self, request, *arg, **kwargs):
        return self.destroy(request, *arg, **kwargs)


#* #################### 
#! 4- CONCRETE VIEWS  
#* ####################
"""# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
#? ListCreateAPIView ve RetrieveUpdateDestroyAPIView'i  import et
# ListCreateAPIView get post işlemini birlikte yapar.
# RetrieveUpdateDestroyAPIView get put delete işlemini birlikte yapar.
#? Bu yöntem 2 veri bekler. 1.  queryset, 2. serializer_class."""

class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#* #################### 
#! 5- VIEWSET  (@action)  
#* ####################

#? Yukardaki tanımlamalara bazı kabiliyetler tanımlamak için @action decorate ile fonksiyon yazabiliriz.

"""# https://www.django-rest-framework.org/api-guide/viewsets/
# - Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

# - Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

# There are two main advantages of using a ViewSet class over using a View class.

#  - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
#  - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

# Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout."""

"""#? ModelViewSet'i import et.
#? ModelViewSet source koduna bakıldığında görülektir ki mixins le beraber yukarıda tanımladığımız fonksiyonlar çalışyor.
#? VIEWSET yöntemi ile tanımlama yapıldığında urls.py'de router tanımlaması yapılması gerekli.
#? @action decorate ile fonksiyon yazarak view'imize bazı kabiliyetler kazandırabiliriz."""

# ?Aşağıda get post işlemi yanında student_count fonksiyonunu yazarak Student tablosundaki öğrenci sayısını return etmiş olduk.
class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # detail=False --> sadece bir öğrenci ile ilgili olmaması. True olsaydı öğrencinin ednPoint'inide göndermek gerekirdi.
    @action(detail=False, methods=["GET"])
    def student_count(self, request):
        count = {
            "student-count" : self.queryset.count()
        }
        return Response(count)
    

# ?Aşağıda get post işlemi yanında student_names fonksiyonunu yazarak seçilen Path'deki öğrenci isimlerini çağırmış olduk. endPoindi --> (..8000/api/path/1/student_names)

class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    
    @action(detail=True)  # default'u get olduğu için  metod adını yazmadık. detail=True olduğu için path ednPoint'inide göndermek gerekiyor.
    def student_names(self, request, pk=None):
        path = self.get_object()
        students = path.students.all()
        return Response([i.first_name for i in students])
    # Respons içerisinde List Comprehensions kullanıldı.
    # path.students.all() içindeki students model içerisindeki related_name='students'dan geliyor.

