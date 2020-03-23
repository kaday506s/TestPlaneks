from celery import shared_task

from apps.users.models import Users, UserVerifications
from apps.users.usecases import SendEmail


@shared_task
def main_schedule_task(user):
    user = Users.objects.get(user.get("username"))
    token, created = UserVerifications.objects.get_or_create(user=user)

    if not created:
        return None

    SendEmail.send(user)
