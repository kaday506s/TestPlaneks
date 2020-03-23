from rest_framework import serializers

from apps.posts.models import Posts, Category, PostsComment
from apps.users.serializers import UserLiteSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class PostsSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # author = UserLiteSerializer()

    class Meta:
        model = Posts
        fields = "__all__"


class PostsCommentSerializer(serializers.ModelSerializer):
    author_comments = UserLiteSerializer()

    class Meta:
        model = PostsComment
        fields = ["text", "date_publication", "author_comments"]

