from rest_framework.serializers import ModelSerializer

from blogs.models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("author", "publication_date")


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("owner", )
