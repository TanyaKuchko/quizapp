from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.username

