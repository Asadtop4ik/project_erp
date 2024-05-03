from rest_framework import permissions


class Manager1Permissions(permissions.BasePermission):
    required_group = 'Manager1'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('erp_system.view_product')
        )


class Manager2Permissions(permissions.BasePermission):
    required_group = 'Manager2'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('erp_system.view_brand')
        )


class Manager3Permissions(permissions.BasePermission):
    required_group = 'Manager3'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('erp_system.view_filial')
        )


class CashierPermissions(permissions.BasePermission):
    required_group = 'Cashier'

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and request.user.is_staff and
                request.user.has_perm('erp_system.view_customer')
        )
