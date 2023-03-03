from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchases, Sales

# pre_save  --> Kaydetmeden önce. Neden Çünkü DB'de null=True eklemesi yapılmadığı için DB'e kaydedilmeden önce hesaplama işleminin yapılması gerekli. null=True olmadığından price tolal oluşturulmadan DB'e kayıt işlemi yapmaz.

@receiver(pre_save, sender=Purchases)
def calculate_total_price(sender, instance, **kwargs):
    instance.price_total = instance.quantity * instance.price

@receiver(pre_save, sender=Sales)
def calculate_total_price(sender, instance, **kwargs):
    instance.price_total = instance.quantity * instance.price

# signal metodunu app.py'e eklemeyi unutma.

 #?------------- blank=True , null=True ----------------
    # blank=True, serializer ile ilgilidir, yani boş bırakılabilir,
    # null=True, DB ile ilgilidir, yani boş bırakılabilir ve DB null kayıt edilir,
    #! eğer sadece  blank=True varsa veri boş gelebilir, ama DB kayıt edilmeden önce
    #! bir işlem/hesaplama vs. yapılıp DB boş/null gitmesini önlemek gerekir.