from rest_framework import serializers
from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    is_available = serializers.BooleanField()
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability',
            'is_available'
        )

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request.user and not request.user.is_staff:  # user true ve staff değil ise. 
            fields.pop('availability')
            fields.pop('plate_number')
        return fields

# availability ve plate_number fieldlerini frontende göstermemek için Yukarıdaki get_fields metodu yerine yeni bir class'da yazabilirdik.

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = (
#             'id',
#             'brand',
#             'model',
#             'year',
#             'gear',
#             'rent_per_day',
#         )

class ReservationSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    #? metod ismi yazmazsak default olarak get_reserved_days olur.
    reserved_days = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ('id', 'customer', 'car', 'start_date', 'end_date', 'total_price', 'reserved_days')
# bir müşteri aynı tarihlerde 1'den fazla rezervasyon yapmaması için.
        #? queryset, hangi tabloya bakacak
        #? fields,  tablodaki hangi fieldlar uniq olacak,  burada üçü aynı anda,
        #? message, uniq değilse, aynı rezervasyandon varsa ne mesaj verecek,
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Reservation.objects.all(),
                fields=('customer', 'start_date', 'end_date'),
                message=('You alreday have a reservation between these dates...')
            )
        ]
    #? Rezervasyon toplam ücreti ne kadar,
    def get_total_price(self, obj):
        return obj.car.rent_per_day * (obj.end_date - obj.start_date).days

    #? Reservasyon süresi toplam kaç gün,
    def get_reserved_days(self, obj):
        return obj.end_date.day - obj.start_date.day