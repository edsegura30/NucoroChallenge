# Python imports
from typing import cast, Any, Dict, Iterable, Optional

# Pip imports
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: Optional[str] = None,
        is_active: bool = True,
        is_staff: bool = False,
        is_superuser: bool = False,
        *args: Iterable,
        **kwargs: Dict,
    ) -> Any:
        """Creates regular user."""
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
        """Creates user with access to back office panel and all permissions."""
        return self.create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            *args,
            **kwargs,
        )


class User(AbstractBaseUser):
    """Currency Exchange API custom user model."""

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

    def __str__(self) -> str:
        if self.first_name:
            return f'{self.first_name}: {self.email}'

        return cast(str, self.email)
