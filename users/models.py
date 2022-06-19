# Pip imports
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    USERNAME_FIELD = 'identifier'

    first_name = models.CharField(
        max_length=140
    )

