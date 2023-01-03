from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') # import etmeyip bu şekildede kullanabiliriz.
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

# Yukarıdaki classı BasePermission sourcecodundan aldık. (Aşağıda) ismini değiştirdik. is_authenticated yerine is_staff yazdık.
# class IsAuthenticatedOrReadOnly(BasePermission):
#     """
#     The request is authenticated as a user, or is a read-only request.
#     """

#     def has_permission(self, request, view):
#         return bool(
#             request.method in SAFE_METHODS or
#             request.user and
#             request.user.is_authenticated
#         )