from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin) 
import jwt
import rest_framework_simplejwt


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`. 
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, name, surname, phone, email, role, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if name is None or surname is None:
            raise TypeError('Users must have a name.')

        if phone is None:
            raise TypeError('Users must have a phone.')

        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(username=username, name=name, surname=surname, phone=phone, role=role, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, surname, username, password, phone, email, role):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        
        if password is None:
            raise TypeError('Superusers must have a password.')

        if username is None:
            raise TypeError('Superusers must have a username.')

        role_obj = Role.objects.get(id=role)

        user = self.create_user(username=username, email=email, password=password, phone=phone, role=role_obj, name=name, surname=surname)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class Role(models.Model):
	name =  models.CharField( max_length = 255)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    role = models.ForeignKey(Role, on_delete = models.CASCADE, related_name='role')
    phone = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'surname', 'phone', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token