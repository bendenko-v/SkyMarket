from rest_framework import permissions

from users.models import UserRoles


class IsOwner(permissions.BasePermission):
    message = 'Updating/deleting not your ad is not permitted'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdmin(permissions.BasePermission):
    message = 'Only admin has permission!'

    def has_permission(self, request, view):
        return request.user.role == UserRoles.ADMIN
