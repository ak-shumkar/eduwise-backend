from rest_framework.permissions import BasePermission


class IsAdministrator(BasePermission):
    message = 'Only admin user can make this request'

    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            return False
        return bool(user.is_superuser)
