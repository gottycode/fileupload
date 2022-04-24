from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from typing import Any, Optional

from django.conf import settings


# ユーザーを作成した後に実行される
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender: str, instance: Optional['User'] = None, created: bool = False, **kwargs: Any) -> None:
    if created and instance is not None:
        # トークンの作成と紐付け
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str) -> 'User':
        user = User(
            email=BaseUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        # トークンの作成
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email: str, password: str) -> 'User':
        u = self.create_user(email=email,
                             password=password)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False
        )
    password = models.CharField(
        _('password'),
        max_length=128
        )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()