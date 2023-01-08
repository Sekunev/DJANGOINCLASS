
#! Coverage 
#! Bu paket test ortamı sağlıyor. Nerelere test yapılması gerektiğinin raporunu sunuyor. Kodumuzun % kaçı test edilmiş, Faremework kullandığımız için örneğin modelviewset bunlar arka planda kendi testlerini yapıyor. Ama override edilen fonksiyonların test edilmesi gerekli.
# Kurulumu:
pip install coverage
# Çalıştır
coverage run manage.py test
# rapor al
coverage report
# Raporu Browserda görmek için
coverage html
# Bu komutla birlkte htmlcov isimli bir klasör oluşuyor içerisindeki index.html dosyasını liveserver ile açabiliyoruz.
# html sayfasında hangi dosyanın % kaç oranında testinin yapıldığı gösteriliyor.
# Tıklandığında detaylar açılıyor. ve test yapılması gereken fonksiyonlar kırmızı ile işaretli olarak gözüküyor.
#! test yapmak için;
# tests isimli bir klasör oluştur.
# default test.py'yi sil.
# tests klasörü içerisinde test yapılacak dosyayı oluştur. test ile başlamak zorunda.(test_flight_api)
# packect olduğunu belirtmek için test klasörü içerisinde __init__.py oluştur.
Bundan sonraki kısım kodlar üzerinden anlatılacak.

from django.urls import reverse
from rest_framework.test import APITestCase,APIRequestFactory, force_authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from flight.views import FlightView
from flight.models import Flight
from rest_framework.authtoken.models import Token
from datetime import datetime, date

class FlightTestCase(APITestCase):
    # - APITestCase --> test için ayrı tablo uluşturup tamamlandığında kaldırıyor.
# Ekte'ki pdf'de classlar yazılı.
    now = datetime.now()  # dinamiz yapı için zaman nesneleri oluşturduk.
    current_time = now.strftime('%H:%M:%S')
    today = date.today()

    def setUp(self):  # sürekli kullanılacak değişkenler setup altında tanımlanıyor. ve aşağıdaki metodlarda kullanılabiliyor.
        self.factory = APIRequestFactory() # HTTP metotlarını simule etmeye yarayan bir oje oluşturuyor.
        self.flight = Flight.objects.create(
            flight_number='123ABC',
            operation_airlines='THY',
            departure_city='Adana',
            arrival_city='Ankara',
            date_of_departure=f'{self.today}',
            etd=f'{self.current_time}',
        )
        self.user = User.objects.create_user(
        username = 'admin',
        password = '123456Aa.'
        )
        # aşağıda kullanmak için flight objesi ve models.User'dan user create ettik.
        self.token = Token.objects.get(user=self.user)

    def test_flight_lis_as_non_auth_user(self):  # tanımlanacak olan metodlar test kword'ü ile başlamalı.
        request = self.factory.get('/flight/flights/')  # yazdığımız endpoint'e factory aracılığı ile get isteği yapıyoruz. #reverse('flights-list')
        print(reverse('flights-list'))
        response = FlightView.as_view({'get': 'list'})(request)  # modelviewset'e özel yaılacak HTTP metodu ve bu metodun neye karşılık geldiğini yazmak gerekiyor.
        print(response)
        self.assertEquals(response.status_code, 200)  # response içerisindeki status_code'un 200 olduğunu kontrol et.
        self.assertNotContains(response, 'reservation') # user staff değil iken reservation field (key) yokmu
        self.assertEqual(len(response.data), 0)  # response.data'nın eleman sayısı 0'a eşitmi. Neden: User staff değil ise geçmiş rezervasyonları görmemesi üzerine kurulu bir dizayn olduğu için. 

# auth ve admin değilsem rezervation gelmeme durumunun testini yapmalıyız.
    def test_flight_list_as_staff_user(self):
        request = self.factory.get('/flight/flights/', HTTP_AUTHORIZATION = f'Token {self.token}')
        # Token ile auth yapmak için endpoint'den sonra yukardaki metodu ekliyoruz.
        self.user.is_staff = True
        self.user.save()  # setUp'da tanımladığımız user'a staff statusu kazandırdık ve kaydettik.
        #force_authenticate(request, user=self.user)  # user'i token olmadan simule authenticate etme metodu .
        request.user = self.user  # request içerisine authenticate ve staff statusu kazandırılmış user'ı ekliyoruz.
        response = FlightView.as_view({'get':'list'})(request)  # yeni request ile  response'ı oluşturuyoruz.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'reservation')   # user staff iken reservation field (key) varmı
        self.assertEqual(len(response.data), 1) # response.data'nın eleman sayısı 1'a eşitmi. Neden: User staff ise geçmiş rezervasyonlarıda görmesi üzerine kurulu bir dizayn olduğu için.

# aşağıda auth olmamış kullanıcılrın post yapamaması gerektiğinin testini yapıyoruz.
    def test_flight_create_as_non_auth_user(self):
        request = self.factory.post(
            '/flight/flights/')
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 401)

# aşağıda auth olmuş ama admin olmayan kullanıcılrın post yapamaması gerektiğinin testini yapıyoruz.
    def test_flight_create_as_auth_user(self):
        request = self.factory.post(
            '/flight/flights/', HTTP_AUTHORIZATION=f'Token {self.token}')

        # request.user = self.user
        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 403)

# staff user creation yapabiliyormu? Bunun testi.
    def test_flight_create_as_staff_user(self):
        # post işlemi için data hazırlıyoruz
        data = {
            "flight_number": "123ABC",
            "operation_airlines": "THY",
            "departure_city": "Adana",
            "arrival_city": "Ankara",
            "date_of_departure": "2022-01-08",
            "etd": "16:35:00",
        }
        # user'in yetkisini staff yapıyoruz.'
        self.user.is_staff = True
        self.user.save()
        request = self.factory.post(
            '/flight/flights/', data, HTTP_AUTHORIZATION=f'Token {self.token}')

        response = FlightView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)

# staff user update (put) yapabiliyormu? Bunun testi.
    def test_flight_update_as_staff_user(self):
        data = {
            "flight_number": "456ewd",
            "operation_airlines": "THY",
            "departure_city": "Adana",
            "arrival_city": "Ankara",
            "date_of_departure": "2022-01-08",
            "etd": "16:35:00",
        }
        print(self.flight.id)

        self.user.is_staff = True
        self.user.save()
        request = self.factory.put(
            '/flight/flights/1/', data, HTTP_AUTHORIZATION=f'Token {self.token}')

        response = FlightView.as_view(
            {'put': 'update'})(request, pk='1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Flight.objects.get(id=1).flight_number, '456ewd')

        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # response = self.client.put(
        #     '/flight/flights/1/', data, format='json')
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(Flight.objects.get().flight_number, '456ewd')


