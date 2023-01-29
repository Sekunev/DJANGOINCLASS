from rest_framework.viewsets import ModelViewSet
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsStaffOrReadOnly
from django.db.models import Q, Exists, OuterRef
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.utils import timezone


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStaffOrReadOnly,)  # [IsStaffOrReadOnly] # Normal kullanıcılar SAFE_METHODS(GET, HEAD, OPTİONS), staff yani admin kullanıcılar tüm crud işlemlerini yapsın.



#! task, can select start and end date and see the list of available cars on selected dates.
    #! availibity staff ise bütün araçları görsün, client sadece müsait olanları görsün diye,
    #? https://yolcu360.com/tr/rent-a-car/ankara-esenboga-havalimani-arac-kiralama/?from=2023-01-27&to=2023-01-29
    #? mesela biz bir tarih aralığı seçince url frontend tarafından yukarıdaki gibi oluşur,
    #? ?from=2023-01-27&to=2023-01-29 soru işaretinden sonra gelenler PARAMETREDİR, from/to, start/end isim önemli değil
    #? girilen bu tarih aralığını yakalamak için  request.query_params.get() kullanılıyor,
    #? query_params bir dictionary olduğundan key'i start veya end olan değerleri alıyoruz,
    #* http://127.0.0.1:8000/api/car/?start=2023-01-15&end=2023-01-20 böyle bir endpoint yazıyoruz bakmak için,

    def get_queryset(self):
        if self.request.user.is_staff:  # staff ise bütün araçları görsün,
            queryset = super().get_queryset()
        else:  # Kullanıcı staff değil ise availability true olan. Yani kiralanabilecek durumda olan araçları queryset'e atadık.
            queryset = super().get_queryset().filter(availability=True)
        # url'de belirli bir tarih aralığında arama yapabilmek için o tarihleri aşağıdaki gibi tanımlıyoruz.
        # ve sadece seçtiği tarih aralığındaki müsait araçları görsün
        # bunun için frontend tarafından gönderilen parametleri yakalıyoruz,
        start = self.request.query_params.get('start')
        #print(start)  # 2023-02-28
        end = self.request.query_params.get('end')
        #print(end)  # 2023-02-30
        #print(self.request)  # <rest_framework.request.Request: GET '/api/car/?start=2023-02-28&end=2023-02-30'>
        #print(self.request.query_params)  # <QueryDict: {'start': ['2023-02-28'], 'end': ['2023-02-30']}>
        
        #? Q parametresi bitwise operatörü ile kullanılır, ???? ne demek?
        #? available olanlar için bir condition yazıyoruz. start_date ve end_date modeldeki fieldler.
        if start is not None or end is not None:
            cond1 = Q(start_date__lt=end)  #less than 9
            cond2 = Q(end_date__gt=start)  #greater than 11

            # not_available = Reservation.objects.filter(
            #     start_date__lt=end, end_date__gt=start
            # ).values_list('car_id', flat=True)  # [1, 2]

            # not_available = Reservation.objects.filter(
            #     cond1 & cond2
            # ).values_list('car_id', flat=True)  # [1, 2]

            # önce Reservasyonlarrdan müsait olmayan araçları yazılan conditionlara göre filitreledi,
            # daha sonra values_list ile sadece bir field aldı, car_id
            # flat=True ise liste olarak dönmesini sağlıyor,
            # sonuçta not_available olarak, müsait olmyan araçların id'lerinin listesi gelir,  [1,2] gibi bir liste dönüyor.

            # ids = id__in=not_available
            # print(not_available)  # <QuerySet [1, 2, 3]>
            #print(ids)  # <QuerySet [1, 2, 3]>

            # queryset = queryset.exclude(id__in=not_available)  # idsi olmayanlar.
            # artık müsait olmayanları bulduğumuza göre, tamamından exclude ile ayırırsak geriye sadece müsaitler kalır.
            queryset = queryset.annotate(
                is_available=~Exists(Reservation.objects.filter(
                    Q(car=OuterRef('pk')) & Q(
                        start_date__lt=end) & Q(end_date__gt=start)
                ))
            )

        return queryset

#  availability ve plate_number fieldlerini frontende göstermemek için bu metodu kullanabilirdik.
    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return CarStaffSerializer
    #     else:
    #         CarSerizlizer

"""#! "__" kullanımı örnekler;
# books = Book.objects.filter(authors__name='John Smith')  # Bu sorgu, John Smith tarafından yazılan tüm kitapları getirecektir.

# books = Book.objects.filter(Q(author__name='John Smith') | Q(author__name='Mary Jones')).filter(pub_date__year=2022)  # Bu sorgu, John Smith veya Mary Jones tarafından yazılan ve 2022 yılında yayınlanan tüm kitapları getirecektir.

#MyModel.objects.filter(id__in=[1,2,3,4])  # id sütununda 1, 2, 3 ve 4 değerlerini içeren tüm nesneleri döndürür."""

""" #!Django filter kullanımı ve kıyaslama operatörleri
people = Person.objects.filter(age__gt=20, name__contains='John') 
Bu kod, 20'den büyük yaşta ve ismi 'John' olanları döndürecektir.
Django, filter() metodunda birçok kıyaslama operatörü sunmaktadır. Örnek olarak:
exact: esitliği kontrol eder.
iexact: case-insensitive esitliği kontrol eder.
contains: bir string içinde arama yapar.
icontains: case-insensitive bir string içinde arama yapar.
gt: büyüklük karşılaştırması yapar.
gte: büyüklük veya eşitlik karşılaştırması yapar.
lt: küçüklük karşılaştırması yapar.
lte: küçüklük veya eşitlik karşılaştırması yapar.
in: belirli bir liste içinde arama yapar.
"""

class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    # kullanıcı staff ise tüm rezervasyonlar staff değil ise kendi rezervasyonlarını görsün.
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(customer=self.request.user)


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        end = serializer.validated_data.get('end_date')
        car = serializer.validated_data.get('car')

        start = instance.start_date
        today = timezone.now().date()
        if Reservation.objects.filter(car=car).exists():
            # a = Reservation.objects.filter(car=car, start_date__gte=today)
            # print(len(a))
            for res in Reservation.objects.filter(car=car, end_date__gte=today):
                if start < res.start_date < end:
                    return Response({'message': 'Car is not available...'})

        return super().update(request, *args, **kwargs)