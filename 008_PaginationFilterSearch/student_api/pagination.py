from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5 #Her sayfada 5 adet.
    page_query_param = 'sayfa' # URL'de page yerine sayfa yazıyor.

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'

class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'
    page_size = 10
    otdering = '-id'