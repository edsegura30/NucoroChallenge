# Python imports
from typing import cast, Any, Dict, Iterable, Optional

# Pip imports
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self,
        email,
        password = None,
        is_active = True,
        is_staff = False,
        is_superuser = False,
        *args,
        **kwargs,
    ):
        """Creates User instance."""
        email = UserManager.normalize_email(email)
        user = self.model(
            email=email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            *args,
            **kwargs
        )

        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email: str, password: str, *args, **kwargs):
        """Creates User with `is_staff` and `is_superuser` flags."""
        return self.create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            *args,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'email'

    email = models.EmailField(primary_key=True, unique=True)
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
