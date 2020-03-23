from django.core.management.base import BaseCommand
from apps.users.models import Group, Users


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        group_low, created = Group.objects.get_or_create(
            name="low", permission=1
        )
        if created:
          print(f"Create Group : {group_low.name}")

        group_a, created = Group.objects.get_or_create(
            name="admin", permission=4
        )
        if created:
            print(f"Create Group : {group_low.name}")

        user, created = Users.objects.get_or_create(
            username="test",
            password="1234",
            group=group_low
        )
        if created:
          print(f"Create User : {user.username} pass: {user.password}")

        user, created = Users.objects.get_or_create(
            username="Admin",
            password="1234",
            group=group_a,
            is_superuser=True
        )
        if created:
          print(f"Create User : {user.username} pass: {user.password}")