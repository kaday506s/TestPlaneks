from enum import Enum


class ErrorMsg(Enum):
    NotToken = "You did not send a token !"
    TokenDoesNotExist = "This token is not in the system !"
    UserPassword = "You did not enter a password !"


class LoggingMsg(Enum):
    LoggingMsg_user_1 = "\nUser ip:({}) try create ==> {}\n "
    LoggingMsg_user_2 = "\nUser created ==> {}\n "

    LoggingMsg_token_1 = "\nToken try activate ==> {}\n"
    LoggingMsg_token_2 = "\nIP ({}) ==> {}\n"

    LoggingMsg_Email_connection = "\nError conn Email ==> {}\n"


class EmailText(Enum):
    title = "-=* Verifications Link *=-"
    message_verification = "*Enter the link -> " \
                           "{}/api/v1/users/activate?" \
                           "token={} "
