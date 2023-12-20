from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from blogs.models import Comment, Post
from blogs.permissions import CommentOwnerPermission, PostOwnerPermission
from blogs.serializers import CommentSerializer, PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    )
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated, PostOwnerPermission)
    authentication_classes = (TokenAuthentication,)
    search_fields = ("title", )
    filter_fields = ("publication_date", )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    )
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated, CommentOwnerPermission)
    authentication_classes = (TokenAuthentication, )
    filter_fields = ("post", "owner")
    search_fields = ("comment", )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
