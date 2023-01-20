from django.contrib import admin
from .models import Product, Review
from django.utils import timezone

# Review içerisinde Products'a ulaşıyorum ancak Products içinde Review'a ulaşamıyorum. Bu sorunu ortadan kaldırmak için. Bu clası yazdıktan sonra inlines keywordu ile göstrilimek istenen clasın altında tanımlamamız gerekli.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ('collapse',)
    min_num = 3
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'is_in_stock', 'update_date', 'added_days_ago', 'how_many_reviews')  # Product Home sayfasında gösterilecek field'ler
    list_editable = ("is_in_stock",)  # edit edilme edilmeme durumu oluşturur.
    # list_display_links = ('create_date',)  # field'i link haline getirir.
    list_filter = ("is_in_stock", "create_date")  # Filtreleme yapar.
    ordering = ('-update_date',)  # Field'e göre sıralama yapar.
    search_fields = ("name",)  # Field'e göre search bar oluşturur.
    prepopulated_fields = {'slug' : ('name',)}  # aralara - koyarak yeni bir bar oluşturur. 
    list_per_page = 25 # 25'li sayfalar halinde göster.
    date_hierarchy = "update_date"  # Field'e göre tarih filtrelemesi
    # fields = (('name', 'slug'), 'description', "is_in_stock") # Objenin içeriğini nasıl görmek istiyorsak.  fieldset kullandığımız zaman bunu kullanamayız

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )

    actions = ("is_in_stock", )
    inlines = (ReviewInline,)

    def is_in_stock(self, request, queryset):
        # print(queryset) <QuerySet [<Product: Diane Ramirez>]>
        count = queryset.update(is_in_stock=True)
        # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#update

        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")

    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
    # Stok2a ekleme fonksiyonu. toolbar'da ' is_in_stock yerine 'İşaretlenen ürünleri stoğa ekle' yazması için.

    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
    # Produk kaç gün önce oluşturuldu. Sayfada görüntülemek için list_display'a ekle.
    added_days_ago.short_description = 'Kaç gün önce eklendi'

    def how_many_reviews(self, obj):
        count = obj.reviews.count()
        return count

    how_many_reviews.short_description = 'Kaç review var'



class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)  # ilgili products'ın id'si gelir



admin.site.register(Product, ProductAdmin)  # oluşturulan clasıda ekle.
admin.site.register(Review, ReviewAdmin)  

admin.site.site_title = "Clarusway Title"  # Site başlığını değiştiriyor.
admin.site.site_header = "Clarusway Admin Portal"  # Giriş sayfasındaki ilk Başlık değişir.
admin.site.index_title = "Welcome to Clarusway Admin Portal"  # Home sayfasındaki başlık değişir.