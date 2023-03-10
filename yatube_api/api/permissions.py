from rest_framework import permissions as p


class IsOwnerOrReadOnly(p.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in p.SAFE_METHODS or obj.author == request.user
