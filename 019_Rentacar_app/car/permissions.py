from rest_framework import permissions

# Normal kullanıcılar SAFE_METHODS(GET, HEAD, OPTİONS), staff yani admin kullanıcılar tüm crud işlemlerini yapsın.
class IsStaffOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
