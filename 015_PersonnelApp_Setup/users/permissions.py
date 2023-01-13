from rest_framework import permissions


# Profil görüntüleme permissions:
# Sadece staff ve request i atan user'la profil sahibi aynıysa görüntüleme hakkı ver.'
class IsOwnerOrStaff(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or (obj.user == request.user))

