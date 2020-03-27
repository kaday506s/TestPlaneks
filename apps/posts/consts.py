from enum import Enum


class ErrorMsg(Enum):
    NoDeleteID = "You did not specify id_delete!"
    DontHavePermissions = "you do not have permission to delete !"
    DoesNotExist = "No comment !"


class EmailTextPosts(Enum):
    title = "-=* New comment on your post *=-"
    MessageNewComment = "*User send comment({}) " \
                        "on your post({})"