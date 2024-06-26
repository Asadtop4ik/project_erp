from rest_framework import permissions


class Manager1Permissions(permissions.BasePermission):
    required_group = 'Manager1'

    def has_permission(self, request, view):
        return (
                request.user.is_superuser or (request.user.is_authenticated and request.user.is_staff and
                                              request.user.groups.filter(name=self.required_group).exists())
        )


class Manager2Permissions(permissions.BasePermission):
    required_group = 'Manager2'

    def has_permission(self, request, view):
        return (
                request.user.is_superuser or (request.user.is_authenticated and request.user.is_staff and
                                              request.user.groups.filter(name=self.required_group).exists())
        )


class Manager3Permissions(permissions.BasePermission):
    required_group = 'Manager3'

    def has_permission(self, request, view):
        return (
                request.user.is_superuser or (request.user.is_authenticated and request.user.is_staff and
                                              request.user.groups.filter(name=self.required_group).exists())
        )
