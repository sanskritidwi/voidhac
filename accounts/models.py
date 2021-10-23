from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):  # Add all required fields
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            password = get_random_string(length=10)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name="Email Address", max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    auth_token = models.CharField(max_length=100, default=True)
    auth = models.BooleanField(default=False)
    name = models.CharField(verbose_name="Name", max_length=50)
    phone = models.CharField(verbose_name="Mobile No.", max_length=13)
    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []   # Required for 'createsuperuser'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_mbile(self):
        return f'{self.mobile}'

    def save(self, *args, **kwargs):
        """For cpanel."""
        self.is_active = (self.is_active is True)
        self.is_staff = (self.is_staff is True)
        self.is_superuser = (self.is_superuser is True)
        self.auth = (self.auth is True)

        super(User, self).save(*args, **kwargs)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=" Name", max_length=50)
    phone = models.CharField(verbose_name="Contact Number", max_length=13)


    def __str__(self):
        return f'{self.name} - {self.user.email}'

    def __str__(self):
        return self.user.email
   

