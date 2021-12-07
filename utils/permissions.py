from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsAdministrator(IsAdminUser):
    message = 'Only admin user can make this request'


class ReadOnlyOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or bool(request.user and request.user.is_staff)


class IsStudentOrAgent(BasePermission):
    message = 'Only students and agents can apply'

    def has_permission(self, request, view):
        user = request.user
        if request.method in SAFE_METHODS:
            return bool(user.is_authenticated)
        return bool(user.is_authenticated and (user.is_student or user.is_agent))

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'user'):
            return obj.user == request.user
