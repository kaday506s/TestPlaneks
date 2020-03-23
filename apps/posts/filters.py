from django_filters import FilterSet, CharFilter
from apps.posts.models import Posts


class PostsFilter(FilterSet):
    name = CharFilter(lookup_expr='iexact')

    class Meta:
        model = Posts
        fields = ["title", "category", "author", "date_publication"]
