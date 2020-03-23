from rest_framework import permissions


class UsersPermissions(permissions.BasePermission):
    """
        Method for checking permissions to user
    """
    def has_permission(self, request, view, *args, **kwargs):

        if request.user.is_anonymous or \
                request.user.is_active:
            return False

        if request.user.is_superuser:
            return True

        return True
