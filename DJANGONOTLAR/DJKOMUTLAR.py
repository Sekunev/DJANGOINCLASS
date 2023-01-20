
#! //*** DJANGO **//
# PYTHON VE PİP SÜRÜMLERİNİ KONTROL
python --version
pip --version

#* SOURCE KODU GÖRMEK İÇİN
CTRL + click
#* PAKETİ KALDIRMAK İÇİN
pip uninstall packedname

# ENV DOSYASINI OLUŞTUR.
python -m venv env
# (bunu yapmamızın sebebi sistemlerin, paketlerin versiyonları değişse bile
# daha sonradan hata vermeden kullanılabilsin diye global'de değil virtual'da çalışmak lazım.)

#* ENV AKTİF ET.
.\env\Scripts\activate
# BASH İLE AKTİF ETMEK İÇİN
source env/Scripts/Activate
# LINUX/MAC
source env/bin/activate

#* AKTİF HALİ PASİF HALE ÇEVİRMEK İÇİN.
deactivate

#* AKTİF ETMEDE SORUN YAŞARSAN AŞAĞIDAKİ KOMUTU ÇALIŞTIR.
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

#* DJANGO İLE RESTFRAMEWORK KURULUMU.
# django'nun API servisi gibi çalışması için bir micro-framework olan;
# restframework kurmak için;
pip install djangorestframework
# sadece yukarıdaki komutu çalıştırsak önce django, sonra restframework kurar.
# daha sonra main/settings.py INSTALLED_APPS içine  'rest_framework', ekle
# tırnak içinde ve mutlaka sonunda virgül ile,
# fakat şu anda main klasörü yok, oluşturunca eklenecek

#* SADECE DJANGO KURULUMU.
pip install django


#* PİP GÜNCEL DEĞİL WARNİNGİ SONRASI PİP GÜNCELLEME.
python -m pip install --upgrade pip

#* YÜKLÜ PAKETLERİ LİSTELER
pip freeze veya pip list

#* PROJEDEKİ PAKETLERİ REQUIREMENTS.TXT'YE YÜKLEME.
pip freeze > requirements.txt
# (bunu yapmamızın sebebi projede kullandığımız paketleri REQUIREMENTS.TXT yükleyerek proje başkaları tarafından clonlandığında paketlerin otamatik projeye yüklenmesini sağlamaktır. Bu yüzden projeyi kapatmadan önce bu işlemi yapmak gerekli.)

#* PULL EDILEN PROJEYI AYAĞA KALDIRMAK IÇIN
pip install -r requirements.txt
# (bunu repodan bir proje indirdiğimizde requirements.txt deki paketleri yüklemek için kullanıyoruz)

#* GİTİGNORE OLUŞTUR.
# googleden ara ve bul. oluşturduğun env dosyası ismi gitignore Environments bölümünde olmalı. env'den farklı bir isim verdiysen gitignore içine ilgili bölüme dosya ismini ekle.
# (https://www.toptal.com/developers/gitignore/api/django)
# (githuba projeyi göndermek için içeriğini toptal gibi sitelerden alabiliriz yada önceki projelerimizden alabiliriz)
# Environments
# .env
# .venv
# env/
# venv/
# ENV/
# env.bak/
# venv.bak/
#? .sekune (mesela böyle bir isim verdiysen .gitignore içindeki bölüme ekle)

#* PROJE OLUŞTUR
django-admin startproject main .
# (içiçe olmadan proje başlatma komutu. eğer nokta koymazsak projeyi içiçe klasör yapısıyla oluşturyor. ilk oluşturmada main dosya ismi tercihi bestpractice.)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework', #! buraya ekle
]

#* APP OLUŞTURMA
python manage.py startapp (appname)
# (appname)appı oluştrduk)(bunu yaptıktan sonra proje dizinine gidip settings.py e girip
# installed appse appimizi tanıtmamız gerekiyor)
 django-admin startapp (appname) --> alternatif.

#* SERVER ÇALIŞTIR
python manage.py runserver
# (SERVERyi ayağa kaldırma default port 8000)

#* SERVER DURDUR
ctrl + C

#* PORT NUMARASINI DEĞIŞTIRME
python manage.py runserver 8080

#* (MAKEMİGRATE) OLUŞTURULAN TABLOLAR İLE İLGİLİ GEREKLİ HAZIRLIKLARI YAP:
python manage.py makemigrations
# (Database'de bi değişiklik yapacaksam bu ve aşağıdaki 2 komutun çalıştırılması gerekli.)
# (app/migrations/ altında 0001_initial isminde bir dosya oluşturarak içerisine model'deki değişiklikleri attı.)

#* (MİGRATE) PAKETLERİN VERİTABANINA AKTARILMASI, TABLOLARIN OLUŞTURULMASI İÇİN. PROJE ÇALIŞTIRIRILIRKEN ALINAN ERRORDAN KURTULMAYI SAĞLAR.
python manage.py migrate

#* SUPERUSER OLUŞTURMA
python manage.py createsuperuser
# 1.python manage.py createsuperuser
# 2.username belirleyin
# 3.emaili bos gecebilirsiniz.
# 4.password yazsaniz da gorunmuyor ama yazabiliyorsunuz, bir sifre belirleyin, tekrar sordugunda ayni sifreyi bir daha yazin
# 5.python manage.py runserver ile tekrar baslatin
# 6.url'nin sonuna admin yazarak login sayfasina gecin
# 7.user ve password bilginizle giris yapin

#* APP/MODEL'İ ADMIN USERDE GÖRMEK İÇİN
# app/admin.py içerisinde import et ve tanımla.
from .models import modelName
admin.site.register(modelName)

#! ORM KOMUTLARINI YAZMAK İÇİN
# https://docs.djangoproject.com/en/4.1/topics/db/queries/
# (shell, django ile komut satırı üzerinden iletişim kurmaya yarar.)
python manage.py shell
exit() #--> Çıkış

from appName.models import className 
s1 = Student.objects.all()
s1 = Student.objects.get(...)
s1 = Student.objects.filter(...)

s1 = Student(first_name='aaa', last_name='a') # atributlara atama yap bu şekilde yapıldığında save etmek gerekli.
s1.number = 8   # atributlara atama yap
s1.save() # Kaydet

s1 = Student.objects.create(first_name="bbb", last_name="b") # create ile atributlara atama yap

s1 = Student.objects.exclude(number=9) # number'i 9 olmayan atribultarı 
s1[0] veya  s1.first() # indexleme, slice'lama veya first() metodu ile ulaşabiliriz.
s1 = Student.objects.filter(number=9) # number'i 9 olan atribultarı bir liste içerisinde döndürür.
s1 = Student.objects.filter(number__gte=9) # number'i 9  ve 9'dan büyük olan atribultarı.
s1 = Student.objects.filter(number__gt=1) # number'i 9'dan büyük olan atribultarı.
s1 = Student.objects.filter(number__lt=9) # number'i 9'dan küçük olan atribultarı.
s1 = Student.objects.filter(first_name__startswith="e") # first_name'i e ile başlayanlar. casesensitive değil(postsql'den dolayı.)
s1 = Profile.objects.get(id=3)  # id'si 3 olan
s1 = Student.objects.get(first_name__exact="sem") # first_name'i sem olan (casesenstive)
s1 = Student.objects.get(first_name__contains="ü") # first_name'i içerisinde ü olan

print(s1.query) # SQL şeklinde içeriğini gösterir.

Parent Modeldeki field'e ulaşma. 005 FBV dersi.
1- Child'deki field'in foreignKey ile tanımlanmış olması gerekli.
2- Child'deki ilgili Field'e ulaş -->  s1 = Student.objects.get(number=36) # <Student: Memal cemal>
3- s1'in bulunduğu tablodaki foreignKey fieldi ve devamında Parent'da hangi stunu istiyorsak erişiyoruz.(number=36 olan öğrencinin Path adı.) --> s1.path.path_name # 'DS'
4- Bir değişkene atayabilirsin. --> path_name = s1.path.path_name # 'DS'
5- Path modelinde "d" ile başlayan fiedler -->  p1 = Path.objects.filter(path_name__startswith="d") --> <QuerySet [<Path: DS>]>
6- Path'i DS olan öğrenciler. --> p1[0].students.all() #  [<Student: s ss>,<Student: Memal cemal>]
7- 6'ncı md. deki students child field'de related_name='students' properties verildiği için kullanıldı.
8- first_name içerisinde e karakteri bulunan öğrenciler. --> p[0].students.filter(first_name__contains="e") # <QuerySet [<Student: Memal cemal>]>

#* PYTHON'DA RESİMLERLE İŞLEM YAPILACAKSA AŞAĞIDAKİ KÜTÜPHANEYİ KUR.
pip install Pillow 
# Sonrasında bazı ayarlar yapmak gerekli.(3 ayar yapılacak.)
# settings.py dosyasına aşağıdaki komutları ekle.
MEDIA_URL = 'media/'  --> yol belirtiyoruz. (1)
MEDIA_ROOT = BASE_DIR / 'media/' --> media'ların yüklendiği root klasörü. Yerel olduğu için media klasörü. (2)
# main urls.py ekle (settings.py de tanımladığımız yolları urls.py de belirtmeliyiz.)(3)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
detay-->https://docs.djangoproject.com/en/4.1/howto/static-files/
# veya
if settings.DEBUG: # dev mode olduğu için.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too. Field silindiğinde Tablonunda silinmesini istiyorsak.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary. Silinecek field'in bağlı olduğu başka tablolarda varsa önce önce onları silmek gerekir.
'''

#* .ENV DEKİ KEYLERİ VE ID'LERI OKUYABİLMEK İÇİN AŞAĞIDAKİ PAKETİ YÜKLE
pip install python-decouple
pip freeze > requirements.txt
# .env'deki key value'si tırnaksız ve = ile arasında boşluk olmayacak.
# sonrasında main/settings.py'de aşağıdaki işlemi yap.
from decouple import config
SECRET_KEY = config("SECRET_KEY")

--CORS-HEADERS;
pip install django-cors-headers
https://github.com/adamchainz/django-cors-headers (README bak)

settings içine;

INSTALLED_APPS = [ "corsheaders",  içine ekle, 

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware", (bu default var, üzerine ekle)

CORS_ALLOW_ALL_ORIGINS = True    #--> ekle en sona

CORS_ALLOW_METHODS = [  
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

ALLOWED_HOSTS = ['*']  --> # olmalı.

#! /////****//////

#* PostgreSQL setup için  (dj-11)
# PYTHON'UN POSTGRES ile çalışmasını sağlamak için;
pip install psycopg2
pip freeze > requirements.txt


#* Swagger için  (dj-11) (endpointler için bir dokuman oluşturmayı sağlıyor.)
# linki => https://drf-yasg.readthedocs.io/en/stable/readme.html
pip install drf-yasg
pip freeze > requirements.txt

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework',
    'drf_yasg',  #! buraya ekle,
  
]

#* main.urls dosyasına aşağıdakinin aynısını kopyala yapıştır.
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin 
from django.urls import path 
 
# Three modules for swagger:
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
 
schema_view = get_schema_view(
    openapi.Info(
    title="Flight Reservation API", 
    default_version="v1",
    description="Flight Reservation API project provides flight and reservation info",
    terms_of_service="#", 
    contact=openapi.Contact(email="rafe@clarusway.com"), # Change e-mail on this line!
    license=openapi.License(name="BSD License"),),
    public=True, 
    permission_classes=[permissions.AllowAny],
    )
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

#! daha sonra dosyaları SAVE ET, ve migrate komutunu çalıştır.
py manage.py migrate


#* Debug Toolbar için  (dj-11) (development aşamasında proje geliştirirken bize yardımcı oluyor)
# linki => https://django-debug-toolbar.readthedocs.io/en/latest/
pip install django-debug-toolbar
pip freeze > requirements.txt

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #thirdparty apps
    'rest_framework',
    'drf_yasg',
    'debug_toolbar',  #! buraya ekle,
  
]
#* main urls.py içindeki urlpatterns içine aşağıdaki path ekle,
# from django.urls import include, eklenmemiş ise #* include import et

from django.urls import path, include
urlpatterns = [
    # path("admin/", admin.site.urls),
    # # Url paths for swagger:
    # path("swagger(<format>\.json|\.yaml)",schema_view.without_ui(cache_timeout=0), name="schema-json"),
    # path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('__debug__/', include('debug_toolbar.urls')), #! buraya ekle, zaten yukarıdakiler vardı.
]

# setting.py içindeki MIDDLEWARE #! en üstüne ekle

MIDDLEWARE = [
'debug_toolbar.middleware.DebugToolbarMiddleware', 
# ...
]

# setting.py içine ekle, yeri önemli değil en sona eklenebilir.
INTERNAL_IPS = [ 
    "127.0.0.1", 
]

#* bütün işlemler tamamlandıktan sonra projeyi çalıştır.
py manage.py runserver

1-admin/
2-swagger(<format>\.json|\.yaml) [name='schema-json']
3-swagger/ [name='schema-swagger-ui']
4-redoc/ [name='schema-redoc']
5-__debug__/

#* yukarıdaki url'ler ve sağ tarafta Debug-toolbar olacak şeklilde gelmesi gerekiyor.

#* eğer Admin panalede CSS yok ise;
python manage.py collectstatic

#! #########################################
#! ŞİMDİ YAPILMIŞ BİR PROJENİN AYRILMASI/PARÇALANMASI NASIL YAPILIR
#! -----------------------------------------

#* Seperate Dev and Prod Settings
1- main klasörü içinde settings isminde yeni bir klasör oluştur.
2- bu yeni klasör içinde 4 tane yeni dosya oluştur, 
  - __ini__.py        #* python dosyası olduğunu belirtmek için
  - dev.py            #* development/geliştirme ortamındaki ayarlar için
  - prod.py           #* product/ürün ortamındaki ayarlar için
  - base.py           #* genel/global ayarları kayıt etmek için
  

#* __init__.py dosyası içine;
from .base import *

env_name = config("ENV_NAME")

if env_name == "prod":
  from .prod import *
  
elif env_name == "dev":
  from .dev import *

  
#* dev.py dosyası içine;
from .base import *

THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
}

INTERNAL_IPS = [
    "127.0.0.1",
    ]


#* prod.py dosyası içine;
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
        "ATOMIC_REQUESTS": True,
        }
    }

#! createsuperuser veya başka kullanıcı oluşturduğumuz zaman,
#! password validasyon ile uğraşmak istemiyorsak bu bölümü sadece prod.py içine koyabiliriz,
#! böylece development aşamasında basit şifre verip geçebiliriz.

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#* base.py dosyası içine;
"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #? my apps
    
    #? trirdpart apps
    'rest_framework',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

#! createsuperuser veya başka kullanıcı oluşturduğumuz zaman,
#! password validasyon ile uğraşmak istemiyorsak bu bölümü base.py'den alıp sadece prod.py içine koyabiliriz,
#! böylece development aşamasında basit şifre verip geçebiliriz.

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

#? for images
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = { 
    "version": 1, 
    # is set to True then all loggers from the default configuration will be disabled. 
    "disable_existing_loggers": True, 
    # Formatters describe the exact format of that text of a log record.  
    "formatters": { 
        "standard": { 
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s" 
        }, 
        'verbose': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        }, 
        'simple': { 
            'format': '{levelname} {message}', 
            'style': '{', 
        }, 
    }, 
    # The handler is the engine that determines what happens to each message in a logger. 
    # It describes a particular logging behavior, such as writing a message to the screen,  
    # to a file, or to a network socket. 
    "handlers": { 
        "console": { 
            "class": "logging.StreamHandler", 
            "formatter": "standard", 
            "level": "INFO", 
            "stream": "ext://sys.stdout", 
            }, 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "verbose", 
            'filename': './debug.log', 
            'level': 'INFO', 
        }, 
    }, 
    # A logger is the entry point into the logging system. 
    "loggers": { 
        "django": { 
            "handlers": ["console", 'file'], 
            # log level describes the severity of the messages that the logger will handle.  
            "level": config("DJANGO_LOG_LEVEL"), 
            'propagate': True, 
            # If False, this means that log messages written to django.request  
            # will not be handled by the django logger. 
        }, 
    }, 
}



# LOGGING link => https://docs.djangoproject.com/en/4.0/topics/logging/#logging


#! pgAdmin uygulamasını aç ve şifreni yazarak giriş yap
#! daha sonra Database üzerine sağ tıklayıp --> create --> database
#! Database ismini yaz, Owner postgres olarak kalacak, başka birşey eklemeden SAVE et.



#! pgAdmin uygulamasından Database oluşturup,
#! settings klasörü içine eklenen 4 yeni dosya içeriği yukarıdaki gibi düzenlendikten sonra;
#* .env dosyası içerisine; aşağıdaki kodları kopyala/yapıştır, (yorumları sil.)

#* base.py
SECRET_KEY=xwyt@lpf1obsnhwbd30g7z(kp7&*4hdyriv%%a0n4@0$59x
DJANGO_LOG_LEVEL=INFO
#? hangi log kayıtlarını tutacak? INFO = herşey
#? DEBUG, INFO, WARNING, ERROR, CRITICAL

#* __init__.py
ENV_NAME=dev
#? PostgreSQL çalışır
# ENV_NAME=dev
#? SQLite çalışır

#* dev.py
DEBUG=True

#* prod.py
SQL_DATABASE=djangotemplate
#? pgAdmin'de oluşturduğumuz database adı
SQL_USER=postgres
#? pgAdmin deki kullanıcı adı (değiştirme)
SQL_PASSWORD=*********
#? pgAdmin'e girdiğimiz şifre
SQL_HOST=localhost
#? burası aynı kalacak (localhost)
SQL_PORT=5432
#? pgAdmindeki default port. eğer değiştirmediysek 5432 kalacak


#! artık main içindeki setting.py dosyasını sil
#* bütün işlemler tamamlandıktan sonra migrate yap, superuser oluştur ve projeyi çalıştır.
py manage.py migrate
py manage.py createsuperuser (daha önceden yapmadıysan)
py manage.py runserver

1-admin/
2-swagger(<format>\.json|\.yaml) [name='schema-json']
3-swagger/ [name='schema-swagger-ui']
4-redoc/ [name='schema-redoc']
5-__debug__/

#* yukarıdaki url'ler ve sağ tarafta Debug-toolbar olacak şeklilde gelmesi gerekiyor.

#* eğer Admin panalede CSS yok ise;
python manage.py collectstatic


#* rest-auth token kullanmak için;
pip install dj-rest-auth
pip freeze > requirements.txt

#* base.py içine ekle
INSTALLED_APPS = (
    ...,
    'rest_framework',                   #? yoksa bunu ekle
    'rest_framework.authtoken',         #? yoksa bunu ekle
    ...,
    'dj_rest_auth', #! bunu ekle
)

#* users app ekle,
python manage.py startapp users

#* base.py içine ekle,
INSTALLED_APPS = (
    #?my apps
    'users',
)

# main urls içinden yönlendirme yap;
urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")), #! bunu ekle,
    ...............
]

#* daha sonra users klasörüne urls.py dosyası oluştur ve içine path ekle;
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# main -> settings kalsörü -> base.py en sonuna ekle,
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}



#* users klasörüne serializers.py dosyası ekle ve içine yapıştır.
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
# resmi doküman : https://www.django-rest-framework.org/api-guide/validators/#validators
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True, 
                                 validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(write_only=True, required=True,
                                   validators=[validate_password], style={"input_type" : "password"} ) 
  password2 = serializers.CharField(write_only=True, required=True, style={"input_type" : "password"}) 
  
  class Meta:
    model = User
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2'
        ]
    
  def validate(self, data):
    if data['password'] != data['password2']:
        raise serializers.ValidationError(
            {'password': 'Password fields didnt match.'}
        )
    return data
    

  def create(self, validated_data): 
    validated_data.pop('password2') 
    password = validated_data.pop('password') 
    user = User.objects.create(**validated_data) 
    user.set_password(password) 
    user.save()
    return user
  


class UserTokenSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ("id", "first_name", "last_name", "email")

class CustomTokenSerializer(TokenSerializer):
  user = UserTokenSerializer(read_only=True)
  
  class Meta(TokenSerializer.Meta):
    fields = ("key", "user")

#* views dosyasına kopyala/yapıştır,
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

class RegisterAPI(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      token = Token.objects.get(user=user)
      data = serializer.data
      data["key"] = token.key
      headers = self.get_success_headers(serializer.data)
      return Response(data, status=status.HTTP_201_CREATED, headers=headers)

      
#* users -> urls dosyasını yeniden düzenle;
from django.urls import path, include
from .views import RegisterAPI

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterAPI.as_view()),
]

      
#* users klasörü içinde signals.py dosyası oluştur ve içine yapıştır.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_Token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
    
#* users apps.py içine kopyala ve yapıştır,
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self) -> None:
        import users.signals



# tekrar migrate yap ve çalıştır.
python manage.py migrate
python manage.py runserver

#* sonuna slash / eklemeyi unutma!!!!
http://127.0.0.1:8000/users/auth/login/
http://127.0.0.1:8000/users/register/

#* dokuman adresinden demo proje indirilip özelliklerine bakılabilir
https://dj-rest-auth.readthedocs.io/en/latest/demo.html
