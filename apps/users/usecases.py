from django.core import mail

from apps.contrib.loggermodule import Logger
from apps.users.consts import LoggingMsg


logging = Logger._logging(__name__)


class SendEmail:

    @staticmethod
    def send(user_email, title, message):
        connection = mail.get_connection()

        try:
            connection.open()
        except Exception as err:
            logging.warning(
                LoggingMsg.LoggingMsg_Email_connection.value.format(err)
            )
            return False

        # email_settings = user_email
        email_settings = "kaday506@hotmail.com"
        email = mail.EmailMessage(
            title, message,
            email_settings,
            [email_settings],
            connection=connection,
        )

        email.send()
        connection.close()

        return True


class UserLogic:
    @staticmethod
    def visitor_ip_address(request):

        x_forwarded_for = request.META.get(
            'HTTP_X_FORWARDED_FOR'
        )

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get(
                'REMOTE_ADDR'
            )
        return ip

