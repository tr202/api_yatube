from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'author',)


class PostSerialiser(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Post
        fields = '__all__'
