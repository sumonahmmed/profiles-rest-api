from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""

        if not email:
            raise ValueError("User must have an active email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save New Superuser with given details"""

        user = self.create_user(email, name, password)


        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)


        return user






class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the System."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve Full Name of user"""

        return self.name

    def get_short_name(self):
        """Retrieve Short Name of user"""

        return self.name


    def __str__(self):
        """Return String representation of our User"""
        return self.name
