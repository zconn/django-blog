from rest_framework import serializers
from blogging.models import Post, Category

class PostSerializer (serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', 'created_date', 'modified_date', 'published_date')


class CategorySerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
