import re

from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerialiser


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_post_id(self):
        pattern = r'posts\/([0-9]+)'
        return re.findall(pattern, self.request.path)[0]

    def get_queryset(self):
        return Comment.objects.filter(
            post=self.get_post_id()).select_related('author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.get_post_id())


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerialiser

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
