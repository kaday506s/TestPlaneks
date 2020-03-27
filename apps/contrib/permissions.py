from rest_framework import permissions
from apps.users.models import Users


class UsersPermissions(permissions.BasePermission):
    """
        Method for checking permissions to user on all routing
    """
    def has_permission(self, request, view, *args, **kwargs):
        if request.user.is_anonymous or \
                not request.user.is_active:
            return False

        if request.user.is_superuser:
            return True
        return True


class UserUpdate(permissions.BasePermission):
    """
        Method to checking permissions to user on update info
    """
    def has_permission(self, request, view, *args, **kwargs):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser:
            return True

        user = Users.objects.get(id=view.kwargs['pk'])
        if user.username == request.user.username:
            return True

        return False


class PostsPermissions(permissions.BasePermission):
    ALLOW_METHOD = ["GET"]
    """
        Method for checking permissions to user on all routing
    """
    def has_permission(self, request, view, *args, **kwargs):

        if request.method in self.ALLOW_METHOD:
            return True

        if request.user.is_anonymous or \
                not request.user.is_active:
            return False

        if request.user.is_superuser:
            return True
        return True
