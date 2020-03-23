from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import Users, Group


class GroupSeri(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    group = GroupSeri()

    class Meta:
        model = Users
        fields = [
                  "username", "id", "middle_name",
                  "phone", "mobile_phone", "group",
                  "first_name", "last_name", "email",
                  "is_active", "middle_name"
                  ]


class UserLiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ["username", "id"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # ToDO have err
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['user'] = {
            "id": self.user.id,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "username": self.user.username,
        }

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

