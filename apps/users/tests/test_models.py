from django.test import TestCase
from apps.users.models import Users, Group


class GroupTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name='GroupTest',
            permission=1234
        )

    def test_model_fields(self):
        self.assertTrue(hasattr(Group, 'name'))
        self.assertTrue(hasattr(Group, 'permission'))

    def test_type_model_fields(self):
        self.assertTrue(
            Group._meta.get_field('name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            Group._meta.get_field('permission').get_internal_type(),
            'IntegerField'
        )

    def test_create_group(self):
        self.assertEqual(str(self.group), self.group.name)


class UsersTest(GroupTest):
    def setUp(self):
        super(UsersTest, self).setUp()

    def test_model_fields(self):
        self.assertTrue(hasattr(Users, 'id'))
        self.assertTrue(hasattr(Users, 'first_name'))
        self.assertTrue(hasattr(Users, 'middle_name'))
        self.assertTrue(hasattr(Users, 'last_name'))
        self.assertTrue(hasattr(Users, 'password'))
        self.assertTrue(hasattr(Users, 'email'))
        self.assertTrue(hasattr(Users, 'is_staff'))
        self.assertTrue(hasattr(Users, 'is_superuser'))
        self.assertTrue(hasattr(Users, 'phone'))
        self.assertTrue(hasattr(Users, 'mobile_phone'))
        self.assertTrue(hasattr(Users, 'group'))

    def test_type_model_fields(self):
        self.assertTrue(
            Users._meta.get_field('id').get_internal_type(),
            'IntegerField'
        )
        self.assertTrue(
            Users._meta.get_field('first_name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('last_name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('password').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('email').get_internal_type,
            'EmailField'
        )
        self.assertTrue(
            Users._meta.get_field('is_staff').get_internal_type,
            'BooleanField'
        )
        self.assertTrue(
            Users._meta.get_field('is_superuser').get_internal_type,
            'BooleanField'
        )
        self.assertTrue(
            Users._meta.get_field('phone').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('username').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('mobile_phone').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('group').get_internal_type,
            'ForeignKey'
        )

    def test_string_representation(self):
        user = Users.objects.create(
            username='User',
            password="1234",
            group=self.group
        )
        self.assertEqual(str(user), user.username)




