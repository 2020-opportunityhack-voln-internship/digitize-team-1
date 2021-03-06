from django.db import models

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, npo, password=None):
        """
        Create custom user with email, first_name, last_name, npo and password fields.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not npo:
            raise ValueError('Users must specify a non-profit')

        if not first_name:
            raise ValueError('Users must specify a first name')

        if not last_name:
            raise ValueError('Users must specify a last name')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            npo=npo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, npo, first_name, last_name, password):
        """
        Creates statf user with custom fields.
        """
        user = self.create_user(
            email,
            password=password,
            npo=npo,
            first_name=first_name,
            last_name=last_name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, npo, first_name, last_name, password):
        """
        Create superuser with custom fields.
        """
        user = self.create_user(
            email,
            password=password,
            npo=npo,
            first_name=first_name,
            last_name=last_name,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    npo = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['npo', 'first_name', 'last_name'] # Email & Password are required by default.

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active