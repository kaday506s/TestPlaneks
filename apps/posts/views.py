from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from django_filters import rest_framework as filters

from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from apps.contrib.permissions import UsersPermissions
from apps.posts.models import \
    Posts, Category, PostsComment

from apps.posts.serializers import \
    PostsSerializer, CategorySerializer, PostsCommentSerializer
from apps.posts.filters import PostsFilter
from apps.users.serializers import UserLiteSerializer


class PostsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):

    queryset = Posts.objects.filter(allow_publication=True)
    serializer_class = PostsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostsFilter
    http_method_names = ["get", "post"]

    permission_classes = (UsersPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data

        data["allow_publication"] = False

        data["author"] = request.user.id
        data["category"] = request.data.get("category_id")

        user_data = PostsSerializer(data=data)
        user_data.is_valid(raise_exception=True)
        user_data.save()

        return Response(user_data.data, status=HTTP_201_CREATED)


class CategoryViewSet(GenericViewSet, ListModelMixin,
                      RetrieveModelMixin, CreateModelMixin):
    permission_classes = (UsersPermissions,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)


class PostsCommentViewSet(GenericViewSet, ListModelMixin,
                      RetrieveModelMixin, CreateModelMixin):
    permission_classes = (UsersPermissions,)

    queryset = PostsComment.objects.all()
    serializer_class = PostsCommentSerializer

