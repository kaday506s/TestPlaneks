from django_filters import rest_framework as filters

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.exceptions import ParseError

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin
)

from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import Users, UserVerifications
from apps.users.serializers import UserSerializer, MyTokenObtainPairSerializer
from apps.users.filters import UserFilter
from apps.users.task import main_schedule_task
from apps.users.consts import ErrorMsg


class UsersViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):

    queryset = Users.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def create(self, request, *args, **kwargs):
        data = request.data

        data["is_active"] = False

        user_data = UserSerializer(data=data)
        user_data.is_valid(raise_exception=True)
        user_data.save()

        main_schedule_task(user_data)

        return Response(user_data.data, status=HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def activete(self, request, **kwargs):
        token = request.data.get("token")

        if not token:
            return ParseError(ErrorMsg.NotToken.value)

        try:
            user_verification = UserVerifications.objects.get(token=token)
        except UserVerifications.DoesNotExist:
            return ParseError(ErrorMsg.TokenDoesNotExist.value)

        user_verification.is_activate = True
        user_verification.user.is_active = True

        user_verification.user.save()
        user_verification.save()

        return Response(status=HTTP_200_OK)


class LoginViewSet(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
