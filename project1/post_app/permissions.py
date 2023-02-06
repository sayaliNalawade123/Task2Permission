from rest_framework import permissions


class IsnamePermission(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.name == str(request.user):
            print('onwer is same as reuester-------')
            return True
        
        return False 