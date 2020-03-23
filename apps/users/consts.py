from enum import Enum


class ErrorMsg(Enum):
    NotToken = "You did not send a token !"
    TokenDoesNotExist = "This token is not in the system !"
