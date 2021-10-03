from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', required=True, queryset=User.objects.all())
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post