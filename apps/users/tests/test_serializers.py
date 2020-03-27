from django.test import TestCase

from apps.users.models import Users, Group
from apps.users.serializers import UserSerializer, GroupSerializer


class GroupSerializerTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name='group_1', permission=1
        )
        self.group_serializer = GroupSerializer(self.group)

    def test_contains_expected_fields(self):
        data = self.group_serializer.data

        self.assertEqual(
            set(data.keys()),
            {'name',  'id', 'permission'}
        )


class UsersSerializerTest(GroupSerializerTest):
    def setUp(self):
        super(UsersSerializerTest, self).setUp()

        self.user = Users.objects.create_user(
            username="test",
            password="1234",
            email="test@mail.re",
            phone="123123123",
            middle_name="Test"
        )
        self.user.group = self.group
        self.user.save()

        self.user_serializers = UserSerializer(self.user)

    def test_contains_expected_fields(self):
        data = self.user_serializers.data

        self.assertEqual(
            set(data.keys()),
            {
             "username", "id", "middle_name",
             "phone", "mobile_phone", "group",
             "first_name", "last_name", "email",
             "is_active", "middle_name"
             }
        )