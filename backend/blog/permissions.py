from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE'] and obj.user == request.user:
            return True