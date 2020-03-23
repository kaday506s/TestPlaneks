from django.core import mail
from apps.users.models import UserVerifications


class SendEmail:

    @staticmethod
    def send(user):
        connection = mail.get_connection()

        try:
            connection.open()
        except Exception as e:
            return False

        title = "Verifications Token"
        user_activ = UserVerifications.objects.get(user=user)
        message = f"Enter the key to confirm {user_activ.token} "

        email_settings = user.email
        email = mail.EmailMessage(
            title, message,
            email_settings,
            [email_settings],
            connection=connection,
        )

        email.send()
        connection.close()

        return True
