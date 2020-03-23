from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from hashlib import md5
from time import time


def random_md5():
    return md5(str(time()).encode()).hexdigest()


class Group(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle name"),
    )
    permission = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Users(AbstractUser):
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle name"),
    )
    email = models.EmailField(
        _('email address'),
        blank=False,
        null=False
    )
    phone = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name=_("Phone"),
    )
    mobile_phone = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name=_("Mobile phone"),
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='group_user',
    )

    class Meta:
        verbose_name_plural = _('Users')
        verbose_name = _('User')

    def __str__(self):
        return self.username


class UserVerifications(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_v',
    )
    token = models.CharField(
        max_length=256,
        unique=True,
        default=random_md5,
        null=False,
        verbose_name=_("token")
    )
    is_activate = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.user.username}-{self.is_activate}"
