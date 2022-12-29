from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5 # Her sayfada 5 adet.
    page_query_param = 'sayfa' # URL'de page yerine sayfa yazıyor.

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10 # sayfada gösterilecek sutun sayısı.
    limit_query_param = 'adet' # URL satısında limit yerine adet yazar.
    offset_query_param = 'baslangic' # URL satısında offset yerine baslangic yazar.

class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'  # URL satırında cursor yerine imleç yazar.
    page_size = 10  # 1 sayfada gösterilecek sutun sayısı
    ordering = "-id"   # id'ye göre tersden sıralama.