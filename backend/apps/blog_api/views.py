from django.views import generic
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer
from .custompermissions import PostUserWritePermission


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class PostDetail(
    generics.RetrieveUpdateDestroyAPIView, 
    ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostUserWritePermission]