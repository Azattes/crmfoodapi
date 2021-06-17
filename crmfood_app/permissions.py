from rest_framework import permissions


class CoachAccessPermission(permissions.BasePermission):
    message = 'Editing players not allowed'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Coach").exists()

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
