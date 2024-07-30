from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def create_user(self, email, password=None, **extra_fields):
        return super().create_superuser(email, password, **extra_fields)


class User(AbstractUser):

    tg_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=255, blank=False, null=True)
    age = models.IntegerField(blank=False, null=True)
    city = models.CharField(max_length=50, blank=False, null=True)
    location = models.CharField(max_length=50, blank=False, null=True)
    sex = models.CharField(max_length=50, blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    first_name = None
    last_name = None
