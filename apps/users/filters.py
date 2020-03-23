from django_filters import FilterSet, CharFilter
from apps.users.models import Users


class UserFilter(FilterSet):
    name = CharFilter(lookup_expr='iexact')

    class Meta:
        model = Users
        fields = "__all__"
