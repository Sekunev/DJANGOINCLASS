from django.shortcuts import render, redirect, get_object_or_404


from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
#? DTL ile yapılması;

#? django bir template ararken app'lerin altındaki templates klasörlerine bakıyor,
#? bunun için app içindeki klasör isminin templates olması ZORUNLU
#? "students/index.html" bunu yazınca bu view bulunduğu app içindeki templates klasörüne bakıyor,
#? yani ; students/templates/students/index.html

def home(request):
        
    #? context yapısı ile kullanılacak değişneknler key/value olarak yazılıp, ilgili html'e aktarılır,
    context = {
        'title': 'clarusway',
        'desc':'This is a Descriptions',
        'number': 123,
        'list1': [1, 2, 3, [1,'a', 2]],
        'dict1': {'key1':'value1', 'key2': 'value2' },
        'dict_list': [
            {'name': 'zed', 'age': 25},
            {'name': 'amy', 'age': 21},
            {'name': 'joe', 'age': 50},
        ]
    }
    #! veya diğer bir yöntem olarak context tanımlamadan render içinde key/value olarak direkt yazılabilirdi;
    # return render(resquest, 'students/index.html', {'title' : 'cooper', 'desc' : 'this is description'})
    
    #? render fonksiyonu aldığı parametreler;
    #* def render(request, template_name, context=None, content_type=None, status=None, using=None)
    # request yani bir istek geldi, 
    # template_name, bu istek gelince hangi template çalışacak,
    # context, ismi değişebilir, template içine değişken aktarmak için key/value şeklinde tanımlanıyor.
    # content_type, status, using, bunlar çok kullanılmıyor, örnek yapılmadı.
    
    #? root'da bulunan templates klasörü içindeki home.html çalışır,
    # return render(resquest, 'home.html', context)

    #? students içinde bulunan templates klasörü içindeki home.html çalışır,
    # return render(resquest, 'students/home.html', context)

    #? root'da bulunan templates klasörü içindeki base.html çalışır,
    # return render(resquest, 'base.html', context)

    #? students içinde bulunan templates klasörü içindeki index.html (root base.html'den inherit edilen) çalışır,
    return render(request, 'students/home.html', context)
    # return HttpResponse('<h1>Hello World!</h1>')


'''
{{ variables }}
değişkenler çift süslü içine yazılır,
başında ve sonunda boşluk bırakılırsa daha iyi olur, bazen hata verebiliyor.
view'da context adı ile, dictionary formatında tanımlanan değişkenin key'ine karşılık gelen value'yi temsil eder,
{{ title }} --> cooper



{% tags %}
[Tags reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-tags)

komutlar açılış/kapanış blokları halinde yazılır,

{% block title %}
Index Home
{% endblock title %}

{% for i in list %}
<li>{{ i }}</li>
{% endfor %}




| -- filter
[Filters reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-filters)

filitreleme için pipe işareti ( | ) kullanılır,
{{ context'ten alınan değişken | yapılacak filitreleme işlemi }}
filter işlemi sadece çıktıyı etkiler, esas değer değişmez

number key'in valuesine 15 ekle, {{ number | add:'15' }}    = 4285+15 ,4300
esas/orjinal value {{ number }}                             = 4285, değişmedi

içinde listeler olan dicti age'e göre sırala; {{ dict_list|dictsort:"age" }}

desc valuesinin ilk 7 karakterini göster ;{{ desc|truncatechars:7 }}
'''

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }

    return render(request, 'students/student_list.html', context)

def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        # print('POST :', request.POST)
        # print('fıles :', request.FILES)
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    context = {
        'form': form
    }

    return render(request, 'students/student_add.html', context)

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    context = {
        'form': form
    }
    return render(request, 'students/student_update.html', context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student
    }

    return render(request, 'students/student_detail.html', context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    context = {
        'student': student
    }
    return render(request, 'students/student_delete.html', context)