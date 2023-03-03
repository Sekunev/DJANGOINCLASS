from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    #? blank yazmazsan zorunlu alan(giriş yapılması gerekli) olarak tanımlanır.
    #? blank: bos alan olup olamama durumu. True yazmazsan boş bırakamazsın uyarı verir. 
    #? null: null degeri alip alamama durumu. İnteger değerli ise ve boş bırakılabilir yani blank=True ise null'da True olmalıdır. Yoksa hata verir.
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='student')
    #? upload_to='student' student isminde bir klasör oluştur ve onun içerisine yükle.
    files = models.FileField(blank=True, null=True, upload_to="student_files")
    register_date = models.DateTimeField(null=True, auto_now_add=True) 
    #? DateTimeField değeri verilen field'den önce başka fieldlere değer ataması yapılmışsa migrate aşamasında hata alınır. Hatada 1 seçeneği seçilebilir. Sonrasında timezone.now seçilir.
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"({self.number}-{self.first_name} {self.last_name})"

    class Meta:
        ordering= ('-first_name',) 
        #! Tersden sıralama için field önüne "-"
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        db_table = "Ögrenciler" # Tablo ismini değiştir.

#! auto_now : Nesne her kaydedildiğinde alanı otomatik olarak şimdi olarak ayarlar.

#! auto_now_add : Nesne ilk oluşturulduğunda alanı otomatik olarak şimdi olarak ayarlayın.

 #?------------- blank=True , null=True ----------------
    # blank=True, serializer ile ilgilidir, yani boş bırakılabilir,
    # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
    #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
    #! bir işlem/hesaplama (signal)vs. yapılıp DB boş/null gitmesini önlemek gerekir.