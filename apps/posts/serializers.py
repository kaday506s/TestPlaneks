from rest_framework import serializers

from apps.posts.models import Posts, Category, PostsComment
from apps.users.serializers import UserLiteSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class PostsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = UserLiteSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"

    def create(self, validated_data):
        validated_data["allow_publication"] = False
        category = validated_data.pop("category", None)

        post = Posts.objects.create(**validated_data)

        if category:
            category, _ = Category.objects.get_or_create(
                category_name=category
            )
            post.category = category

        post.save()
        return post


class PostsCommentSerializer(serializers.ModelSerializer):
    author_comments = UserLiteSerializer(read_only=True)

    class Meta:
        model = PostsComment
        fields = ["id", "text", "date_publication", "author_comments"]

    def create(self, validated_data):

        post = PostsComment.objects.create(**validated_data)
        post.save()

        return post
