from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blogging.models import Post, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class PostSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'author', 'text', 'created_date', 'modified_date', 'published_date')


class CategorySerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'posts')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
