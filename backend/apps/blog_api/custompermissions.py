from rest_framework import permissions


class PostUserWritePermission(permissions.BasePermission):
    message = 'Only authors of posts are allowed to edit them.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


# class PostUserWritePermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return True
#         return False