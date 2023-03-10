from rest_framework import serializers as s

from posts.models import Comment, Group, Post


class GroupSerializer(s.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(s.ModelSerializer):
    author = s.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class PostSerialiser(s.ModelSerializer):
    author = s.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'
