from celery import shared_task
from django.conf import settings
from config.celery import app

from apps.users.models import UserVerifications
from apps.users.usecases import SendEmail
from apps.users.consts import EmailText


@app.task
def main_schedule_task(users):

    user_verifications = UserVerifications.objects.get(
        user__username=users.get('username')
    )
    res = SendEmail.send(
        user_verifications.user.email,
        EmailText.title.value,
        EmailText.message_verification.value.format(
            settings.BASE_URL, user_verifications.token
        )
    )
    if res:
        user_verifications.is_send_mail = True
        user_verifications.save()


@shared_task
def check_send_mail():
    user_verifications = UserVerifications.objects.filter(
        is_send_mail=False
    )
    for verification in user_verifications:
        res = SendEmail.send(
            user_verifications.user.email,
            EmailText.title.value,
            EmailText.message_verification.value.format(
                settings.BASE_URL, verification.token
            )
        )
        if res:
            user_verifications.is_send_mail = True
            user_verifications.save()
