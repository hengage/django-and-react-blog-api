from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author' , 'excerpt', 'content', 'status')