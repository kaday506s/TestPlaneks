from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ParseError

# My modules
from apps.contrib.permissions import PostsPermissions
from apps.posts.models import (
    Posts,
    Category,
    PostsComment
)
from apps.posts.serializers import (
    PostsSerializer,
    CategorySerializer,
    PostsCommentSerializer
)
from apps.posts.consts import ErrorMsg, EmailTextPosts
from apps.posts.filters import PostsFilter
from apps.posts.task import main_schedule_task_comments


class PostsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):

    queryset = Posts.objects.filter(allow_publication=True)
    serializer_class = PostsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostsFilter

    permission_classes = (PostsPermissions,)

    def create(self, request, *args, **kwargs):
        """
                {"title": "title name", "text": "text"}

            -- and optional

                "image": "***"
        """
        data = request.data

        category = request.data.get("category")

        posts_data = PostsSerializer(data=data)
        posts_data.is_valid(raise_exception=True)
        posts_data.save(
            author=request.user,
            category=category
        )

        return Response(posts_data.data, status=HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def get_comments(self, request, **kwargs):
        data_posts_comments = PostsComment.objects.filter(
            posts__id=self.kwargs["pk"]
        )
        post_comment_data = PostsCommentSerializer(
            data_posts_comments,
            many=True
        )

        return Response(post_comment_data.data, status=HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def create_comments(self, request, **kwargs):
        """
            {"text":"text"}
        """
        data = request.data

        post_comment_data = PostsCommentSerializer(data=data)
        post_comment_data.is_valid(raise_exception=True)

        current_posts = self.get_object()

        post_comment_data.save(
            author_comments=request.user,
            posts=current_posts
        )
        print(current_posts.title)
        print(current_posts.author)
        print(EmailTextPosts.MessageNewComment.value.format(data.get('text'),current_posts.title))
        main_schedule_task_comments.delay(
            data.get('text'),
            current_posts.title,
            current_posts.author.email
        )
        return Response(post_comment_data.data, status=HTTP_201_CREATED)

    @action(detail=True, methods=["delete"])
    def delete_comments(self, request, **kwargs):
        """
            link with query params
                /api/v1/posts/2/delete_comments?id_delete=3
        """
        id_delete = request.query_params.get("id_delete")

        if not id_delete:
            return ParseError(ErrorMsg.NoDeleteID.value)

        try:
            post = PostsComment.objects.get(
                id=id_delete, posts=self.get_object()
            )
        except PostsComment.DoesNotExist:
            return ParseError(ErrorMsg.DoesNotExist.value)

        if request.user.is_superuser or \
                post.author_comments.username == request.user.username:
            post.delete()
            return Response(status=HTTP_200_OK)

        return ParseError(ErrorMsg.YouDontHavePermissions.value)


class CategoryViewSet(GenericViewSet, ListModelMixin,
                      RetrieveModelMixin):

    permission_classes = (PostsPermissions,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)

