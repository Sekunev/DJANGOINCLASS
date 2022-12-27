from rest_framework import serializers
from .models import Student, Path

#! Serializers nedir:
# Database'de complex type --> Queryset formatında bulunan verinin frontend'de kullanılabilir hale getirmek için JSON formatına çeviren yapı.
#! API nedir:
# Uygulanaların birbirleri ile iletişime geçebilmeleri için gerekli arayüz.

#! Ekleme özelliği
# Serializers ile DB'den Frontend'e veya Frontend'den DB'e veri aktarırken veri ekleme ve çıkarma işlemi yapabiliyoruz. Ancak DB'e kaydetme işleminde model'de hangi Field varsa onları ekleyebiliyoruz.


#? StudentSerializer'i aşağıda mantığını anlamak için ilkel yöntemle oluşturduk. Bu ilkel yöntemde oluşturduğumuzda create ve update metodlarınıda oluşturmamız gerekli. atribute'ların türünü ise model ile uyumlu yapmak gerekli yoksa çalışmaz.
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()
#? atribute'ların türünü ise model ile uyumlu yapmak gerekli yoksa çalışmaz.
    
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#? **validated_data --> Yukarıdaki field'lerin açılmış hali.

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance


#? ModelSerializer' dan üretilen StudentSerializer'da create ve update metodlarını ile Field'leri ayrıca tek tek yazmaya gerek yok. Kendi içerisinde bunları oluşturuyor.
# Benden ne bekliyor.
# 1- Model ismi.
# 2- Hangi Field'lar.
class StudentSerializer(serializers.ModelSerializer):

    # Model'de olmamasına rağmen born_year'ı ekleme.
    # önce Field metodlarından SerializerMethodField'ı kullanıyoruz.
    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    # SerializerMethodField'ı kullandığım için metod bekliyor.
    # Sonrasında metod field yazarak frontend'e gönderebiliyorum. metodun başında get unutulmamalı.

    born_year = serializers.SerializerMethodField() # read only.
    path = serializers.StringRelatedField()  # read only. Sadece okunabilir. StringRelatedField --> string model/ __str__de olanı döndürür. Bu metod yazılmadan çağırıldığında id döner. 
    # path_id = serializers.IntegerField() # not read only. Böyle Push yapılabilir. çünkü not read only. 

    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["first_name", "last_name","number", "age", "born_year", "path", "path_id"] # sadece .. kadar field'e getir.
        # exclude = ["number"]  # number dışındaki hepsi.

    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now() #Şimdiki zaman
        return current_time.year - obj.age


#! Nested Serializer

class PathSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    # Bu path'de (Fullstack) birden fazla student olacağı için  many=True yazdık. Böylece Hangi patte hangi öğrenciler olduğunu görmüş olduk.

    students = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detail'
    )
    # HyperlinkedRelatedField ile her öğrencinin url'sini çağırmış oluyoruz. view_name='detail' deki datail den geliyor.

    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]