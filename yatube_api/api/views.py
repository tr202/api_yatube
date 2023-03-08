import re

from rest_framework import viewsets
from rest_framework import permissions

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerialiser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_post(self):
        pattern = r'posts\/([0-9]+)'
        post_id = re.findall(pattern, self.request.path)[0]
        return Post.objects.get(pk=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return super().get_queryset().filter(post=self.get_post().pk)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerialiser

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
