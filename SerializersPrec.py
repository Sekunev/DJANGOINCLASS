Serializers

Web geliştirmede, birçok uygulama, ön ucun arka uçla konuşmasına izin vermek için REST API'lerine güvenir. Bir React uygulaması dağıtıyorsanız, React'in veritabanından bilgi kullanmasına izin vermek için bir API'ye ihtiyacınız olacaktır.

Veritabanındaki veriler ön uca JSON, XML veya diğer içerik türleri biçiminde aktarılır. Ama bildiğiniz gibi veritabanlarımızdaki veriler bu formatta değil. Seri hale getiriciler , veritabanlarındaki karmaşık verilerin, daha sonra kolayca JSON, XML veya diğer içerik türlerine dönüştürülebilen yerel Python veri türlerine dönüştürülmesine olanak tanır. Seri hale getiriciler aynı zamanda, gelen verileri doğruladıktan sonra ayrıştırılan verilerin tekrar karmaşık türlere dönüştürülmesine izin vererek seri durumdan çıkarma sağlar.

REST çerçevesindeki seri hale getiriciler, Django'nun Form ve ModelForm sınıflarına çok benzer şekilde çalışır. Bir Serializer sınıfı sağlıyoruz ve modelimize göre alanlar oluşturuyoruz. Modelimizi hatırlayalım:

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()    

Ardından fscohort_api klasörümüzde bir serializers.py dosyası oluşturalım. Student nesnelerine karşılık gelen verileri seri hale getirmek ve serisini kaldırmak için kullanabileceğimiz bir seri hale getirici ilan edeceğiz . Bir seri hale getirici bildirmek, bir form bildirmekle çok benzer:

from rest_framework import serializers

class StudentDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    number = serializers.IntegerField()

NOT: Modelde otomatik olarak oluşturulan id'leri seri hale getirip ön uca göndermek faydalı olacaktır.

Nesneleri Serileştirme
Artık bir Öğrenciyi veya Öğrenci listesini seri hale getirmek için StudentDefaultSerializer'ı kullanabiliriz. Yine Serializer sınıfını kullanmak, Form sınıfını kullanmaya çok benziyor.

serializer = StudentDefaultSerializer(student)
serializer.data
# {'id': '1', 'first_name': 'Edward', 'last_name': 'Benedict', 'number':'123'}

Bu noktada, model örneğini Python yerel veri türlerine çevirdik . Serileştirme sürecini sonlandırmak için verileri JSON'a dönüştürüyoruz .

from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
json
# b'{"id":"1","first_name":"Edward","last_name":"Benedict","number":"123"}'


Nesnelerin serisini kaldırma
Serileştirme benzerdir. İlk olarak, bir akışı Python yerel veri türlerine ayrıştırıyoruz...

import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)


...sonra bu yerel veri türlerini doğrulanmış verilerden oluşan bir sözlüğe geri yükleriz.

serializer = StudentDefaultSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# {'id': '2', 'first_name': 'Walter', 'last_name': 'White', 'number':'321'}


Örnekleri kaydetme
Doğrulanmış verilere dayalı olarak eksiksiz nesne örneklerini döndürebilmek istiyorsak, .create() and .update() yöntemlerinden birini veya her ikisini uygulamamız gerekir.

Nesne örnekleriniz Django modellerine karşılık geliyorsa, bu yöntemlerin nesneyi veritabanına kaydettiğinden de emin olmak isteyeceksiniz. Örneğin, Student bir Django modeliyse (Projemizde bu bir modeldir), yöntemler şöyle görünebilir:

def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance


.save() Artık verileri seri durumdan çıkarırken , doğrulanmış verilere dayalı olarak bir nesne örneğini döndürmek için arayabiliriz .

student = serializer.save()

Çağırma .save() , serileştirici sınıfı başlatılırken mevcut bir örneğin geçirilip geçirilmediğine bağlı olarak yeni bir örnek oluşturur veya mevcut bir örneği günceller:

# .save() will create a new instance.
serializer = StudentDefaultSerializer(data=data)

# .save() will update the existing `student` instance.
serializer = StudentDefaultSerializer(student, data=data)


Hem .create() ve .update()yöntemleri isteğe bağlıdır. Seri hale getirici sınıfınızın kullanım durumuna bağlı olarak, bunların hiçbirini, birini veya her ikisini birden uygulayabilirsiniz.

Doğrulama
is_valid()Verilerin serisini kaldırırken , doğrulanmış verilere erişmeye veya bir nesne örneğini kaydetmeye çalışmadan önce her zaman aramanız gerekir . Herhangi bir doğrulama hatası oluşursa, .errors özelliği sonuçta ortaya çıkan hata mesajlarını temsil eden bir sözlük içerecektir. Örneğin:

serializer = StudentDefaultSerializer(data={'first_name': 'victor', 'last_name': 'Hugo'})
serializer.is_valid()
# False
serializer.errors
# {'first_name': ['Enter a valid first_name.'], 'number': ['This field is required.']}

Bir önceki sayfada seri hale getiricilerin Django'daki Form yapılarına çok benzediğini söylemiştik. Formlardaki gibi elimizdeki Student modelini kullanarak bir serializer sınıfı yapmak mümkündür. Bunu, Django'nun Model formlarına çok benzer şekilde çalışan seri hale getiricileri bildirerek yapabiliriz. ModelSerializer sınıfı, Model alanlarına karşılık gelen alanlarla otomatik olarak bir Serializer sınıfı oluşturmanıza olanak sağlayan bir kısayol sağlar.

ModelSerializer sınıfı, aşağıdakiler dışında normal bir Serializer sınıfıyla aynıdır:

Modele bağlı olarak sizin için otomatik olarak bir dizi alan oluşturacaktır.
Seri hale getirici için unique_together doğrulayıcılar gibi otomatik olarak **doğrulayıcılar** oluşturur.
Basit varsayılan uygulamalarını içerir. create()ve .update().
Bir ModelSerializer bildirmek şuna benzer:

from rest_framework import serializers
from fscohort.models import Student

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'number']

Varsayılan olarak, sınıftaki tüm model alanları karşılık gelen seri hale getirici alana eşlenecektir.

rest_framework modülünden serializer sınıfını içe aktardık.
Daha sonra serializer istediğimiz modeli import ettik.
Ardından, model form sınıfı gibi, bir seri hale getirici sınıf oluşturduk. Buna model seri hale getirici sınıfı denir.

Diğer Serizizer Türleri

NOT : Diğer serileştirici Türleri ileri düzey konulardır ve ayrıntılı bilgi için belgelere bakabilirsiniz.

HyperlinkedModelSerializer

HyperlinkedModelSerializer sınıfı, ilişkileri temsil etmek için birincil anahtarlar yerine köprüler kullanması dışında ModelSerializer sınıfına benzer.

Varsayılan olarak seri hale getirici, birincil anahtar alanı yerine bir url alanı içerecektir.

Url alanı, bir HyperlinkedIdentityField seri hale getirici alanı kullanılarak temsil edilecek ve modeldeki herhangi bir ilişki, bir HyperlinkedRelatedField seri hale getirici alanı kullanılarak temsil edilecektir.

Birincil anahtarı alanlar seçeneğine ekleyerek açıkça dahil edebilirsiniz, örneğin:

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'id', 'first_name', 'last_name', 'number']

Bir HyperlinkedModelSerializer örneğini başlatırken, geçerli isteği seri hale getirici bağlamında içermelisiniz, örneğin:

serializer = StudentSerializer(queryset, context={'request': request})

Bunu yapmak, hiper bağlantıların uygun bir ana bilgisayar adını içerebilmesini sağlar, böylece ortaya çıkan temsil, aşağıdakiler gibi tam nitelikli URL'ler kullanır:

http://api.example.com/students/1/

Göreceli URL'ler yerine, örneğin:

/students/1/

ListeSerializer

ListSerializer sınıfı, birden çok nesneyi aynı anda serileştirme ve doğrulama davranışını sağlar. Genellikle ListSerializer'ı doğrudan kullanmanız gerekmez, bunun yerine bir seri hale getirici başlatırken many=True iletmeniz yeterlidir.

Bir seri hale getirici başlatıldığında ve many=True iletildiğinde, bir ListSerializer örneği oluşturulur. Serileştirici sınıfı daha sonra üst ListSerializer öğesinin çocuğu olur.

Aşağıdaki bağımsız değişken, bir ListSerializer alanına veya many=True iletilen bir serileştiriciye de iletilebilir:

allow_empty Bu, varsayılan olarak Doğru'dur, ancak boş listelerin geçerli girdi olarak izin vermemesini istiyorsanız, Yanlış olarak ayarlanabilir.

BaseSerializer

Alternatif seri hale getirme ve serisini kaldırma stillerini kolayca desteklemek için kullanılabilen BaseSerializer sınıfı. Bu sınıf, Serileştirici sınıfıyla aynı temel API'yi uygular Serileştirici sınıfının desteklemesini istediğiniz işlevselliğe bağlı olarak geçersiz kılınabilen dört yöntem vardır:

.to_representation() - Okuma işlemleri için serileştirmeyi desteklemek üzere bunu geçersiz kılın.
.to_internal_value() - Yazma işlemleri için seri durumdan çıkarmayı desteklemek için bunu geçersiz kılın.
.create() ve .update() - Örnekleri kaydetmeyi desteklemek için bunlardan birini veya her ikisini geçersiz kılın. Bu sınıf, Serializer
sınıfıyla aynı arabirimi sağladığından, onu mevcut genel sınıf tabanlı görünümlerle tam olarak normal bir Serializer veya ModelSerializer için yaptığınız gibi kullanabilirsiniz .
Bunu yaparken fark edeceğiniz tek fark, BaseSerializer sınıflarının göz atılabilir API'de HTML formları oluşturmamasıdır. Bunun nedeni, döndürdükleri verilerin, her alanın uygun bir HTML girdisine dönüştürülmesine izin verecek tüm alan bilgilerini içermemesidir.



Üçüncü taraf paketleri
Üçüncü taraf paketleri de mevcuttur.

Serileştirici Alanları
Django'daki Model alanları ve Form alanları gibi, seri hale getiricilerin de alanları vardır. Seri hale getirici alanları, ilkel değerler ve dahili veri türleri arasında dönüştürmeyi işler. Ayrıca, giriş değerlerini doğrulamanın yanı sıra ana nesnelerinden değerleri alma ve ayarlama ile de ilgilenirler.
Not: Seri hale getirici alanları, field.py'de bildirilir, ancak kural gereği bunları kullanarak içe aktarmalı from rest_framework import serializersve alanlara şu şekilde başvurmalısınız serializers.FieldName. Örneğin:

class StudentDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()  


Temel Argümanlar
read_only , write_only, gerekli, varsayılan, allow_null, kaynak, doğrulayıcılar, hata_mesajları, etiket, yardım_metni, başlangıç, stil örneğin:

# Use  for the input.
password = serializers.CharField(
    style={'input_type': 'password'}
)

ALANLAR
Model ve form alanlarına benzer serileştirici alanları şunları içerir:

Boole Alanı
CharField
SlugField
TamsayıAlanı
TarihSaatAlanı
...