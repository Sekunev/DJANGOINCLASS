# Class Based Views
# Class-Based yapısını kullanarak, önceki sayfada Function Base yapısını kullandığımız aynı işlemleri yapıyoruz. Aşağıda da görebileceğiniz gibi daha düzenli bir kod yapısı sağlıyor. Mantık ve kodlar hemen hemen aynı. Kodları inceleyin lütfen.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer
from fscohort.models import Student


class StudentList(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        serializer =StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentGetUpdateDelete(APIView):
    
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        #student = get_object_or_404(Student, id=id)
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def post(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message":"Student updated"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def  delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# - line 3 We imported APIVıew class and inherited our classes from APIVıew class.

# Then configure our urls.py file:

from django.urls import path
from . import views as api_views

urlpatterns = [
    path("", api_views.StudentList.as_view(), name="list"),
    path("/", api_views.StudentGetUpdateDelete.as_view(), name="detail"),
]

# When you go to http://127.0.0.1:8000/api/ you can see a browsable API from the DRF and the same result as Functional Base views

# Generic Views And Mixins

Django'da CRUD işlemleri için gerçekleştirdiğimiz işlemler genel olarak benzer işlemler olduğu için arka planda bu işlemleri bizim yerimize gerçekleştiren yapılar geliştirilmiştir. Bu sayede aynı kodları tekrar yazmaktan kurtulmuş oluyoruz ve aynı işi daha az kod ile yapmış oluyoruz.
Bu amaçla DRF tarafından GenericAPIViews ve Mixins oluşturulmuştur. Jenerik APIView'lar, Sınıf Tabanlı Görünümlerde kullandığımız APIView'dan devralınır ve onlara ekstra özellikler verir. GenericApiView'ler genellikle karışımlarla birlikte kullanılır. Mixins, GenericAPIViews'a ekler ve yetenekler sağlar. Bunları şöyle düşünebilirsiniz ve GenericAPIViews ve Mixins ile aynı işlemleri yazalım:.create().list() .get().post()

from fscohort.models import Student
from .serializers import StudentSerializer
from rest_framework import generics, mixins

class StudentDetail(generics.GenericAPIView,mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin ):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"
    
    def get(self, request, id):
        return self.retrieve(request)
             
    def put(self, request, id):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request,id)


class Student(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
 
        
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

# line 3 we imported generics and mixins from rest_framework
# line 7 we define the serializer_class (the name is standard) which we created before.
# line 8We define the query_set (the name is standard) according to the view logic we will set up
# line 9Lookup_field: It specifies which field we will call the objects from. It should be unique
# NOTE: We use lookup_field and id as we will call a specific object for GET, PUT, DELETE operations from django.urls import path from .views import Student, StudentDetail Let's configure urls.py file :

urlpatterns = [
    path("list/", Student.as_view(), name="list"),
    path("", StudentDetail.as_view(), name="detail"),
]

# http://127.0.0.1:8000/api/list adresine gittiğinizde, DRF'den göz atılabilir bir API, Öğrenci listesi ve öğrenci oluşturmak için bir form

# görebilirsiniz. Belirli bir öğrenci nesnesini görüntülemek istiyorsanız, kimliğini kullanmalısınız. öğrenci. Örneğin http://127.0.0.1:8000/api/16 uç noktası bize id numarası 16 olan öğrenciyi getiriyor

# . Gözatılabilir API'de bu öğrenci için GET, PUT, DELETE seçeneklerini görebiliyoruz.

# Concrete Views

# GenericAPIView ve Mixins ile arka planda neler olduğunu öğrendik. Temel amacımız Somut görüşleri öğrenmektir . Somut görünümler bize ihtiyacımız olan tüm işlevselliği çok daha az kodla sunuyor.

# Her somut görünüm, bir GenericAPIView ve ilişkili Karışımlardan oluşur. örneğin: ListCreateApiView , ListModelMixin , CreateModelMixin ve GenericAPIView öğelerinin birleşimidir . 


# Dolayısıyla, ConcreteView'ler yazması ve okuması en kolay görünümlerdir . Aynı işlemleri somut görünümlerle kodlayalım

from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    

class StudentGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"

# urls.py dosyasını yapılandıralım:
urlpatterns = [
    path("list/", StudentList.as_view(), name="list"),
    path("list/", StudentGetUpdateDelete.as_view(), name="detail"),

]