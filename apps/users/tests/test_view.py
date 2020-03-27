from django.test import RequestFactory, TestCase
from apps.users.models import Users, Group
from rest_framework.test import force_authenticate, APIRequestFactory
from apps.users.views import UsersViewSet, UsersUpdateViewSets
import json


class TestUsersViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.group = Group.objects.create(
            name='org_1', permission=1
        )

        self.users_attributes = {
            'id': '1',
            'username':"username",
            'first_name': 'user_test_notadmin',
            'last_name': 'user_test_notadmin',
            'email': 'usernotadmin@ukr.ua',
            'is_staff': True,
            'is_superuser': False,
            'is_active': True,
            'phone': '38033663366',
            'mobile_phone': '55665566',
            'group': self.group,

        }
        self.users_attributes_2 = {
            'id': '2',
            'username': "username_l",
            'first_name': 'test_notadmin',
            'last_name': 'test_notadmin',
            'email': 'user@ukr.ua',
            'is_staff': True,
            'is_superuser': False,
            'is_active': True,
            'phone': '234234',
            'mobile_phone': '33663366',
            'group': self.group,

        }
        self.url = f"/api/v1/users/{self.users_attributes['id']}"
        self.url_patch = f"/api/v1/user/{self.users_attributes['id']}"

        self.users = Users.objects.create_user(**self.users_attributes)
        self.users_2 = Users.objects.create_user(**self.users_attributes_2)

    def test_for_method_get(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.users)
        view = UsersViewSet.as_view({'get': 'retrieve'})

        response = view(request, pk=self.users_attributes['id']).render()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], int(self.users.id))

    def patch_method(self, user):
        self.data_change = {'first_name': "Test_OK"}
        request = self.factory.patch(
            self.url_patch,
            self.data_change,
            content_type='application/json'
        )
        force_authenticate(request, user=user)
        view = UsersUpdateViewSets.as_view(
            {'patch': 'partial_update'}
        )

        response = view(
            request, pk=self.users_attributes['id']
        ).render()

        response_content = json.loads(
            response.content.decode()
        )
        return response, response_content

    def test_path_user_access(self):

        response, response_content = self.patch_method(self.users)
        self.assertEqual(
            response.status_code, 200
        )

        self.assertEqual(
            response_content['first_name'],
            self.data_change['first_name']
        )

    def test_path_user_bad_access(self):
        response, response_content = self.patch_method(self.users_2)

        self.assertEqual(
            response.status_code, 403
        )
