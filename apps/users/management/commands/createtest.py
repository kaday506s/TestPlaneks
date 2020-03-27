from django.core.management.base import BaseCommand
from apps.users.models import Group, Users


class Command(BaseCommand):

    def _create_group(self, name, permission):
        group, created = Group.objects.get_or_create(
            name=name, permission=permission
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                  f"Create Group : {group.name}- "
                  f"permission lvl {group.permission}"
                )
            )

        return group

    def _create_user(self, name, password, group):
        try:
            user = Users.objects.create_user(
                username=name,
                password=password
            )
        except Exception as err:
            self.stdout.write(
                self.style.ERROR(
                    err
                )
            )
            return None

        user.grop = group
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Create User : {user.username}"
            )
        )

    def handle(self, *args, **kwargs):
        group = self._create_group(
            name="low", permission=1
        )

        self._create_user("admin", "1234", group)

        group = self._create_group(
            name="Medium", permission=2
        )

        self._create_user("Medium_Users", "1234", group)
