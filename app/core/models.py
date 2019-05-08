from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    """Manager provide the helpers functions for create user or super users"""

    def create_user(self, email, password=None, **extra_fields):
        """ **extra_fields take other params send to model and fill the table """
        if not email:
            raise ValueError('Users must have ana email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ **extra_fields take other params send to model and fill the table """

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # define the user manager class for User
    objects = UserManager()

    # necessary to use the django authentication framework: this field is used as username
    USERNAME_FIELD = 'email'

