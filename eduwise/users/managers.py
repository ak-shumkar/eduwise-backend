from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Django requires the environment `User`
    evaluated their own Manager class.
    Inherited from BaseUserManager, we reuse a lot of codes,
    regular Django to create a `User`.

    All we have to do is redefine the function
    `create_user` which we will use
    to create `User` objects.
    """

    def _create_user(self, username, password=None, **extra_fields):

        if not username:
            raise ValueError('Username is required')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and returns a `User` with an email address and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and returns a user with superuser (administrator) rights.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)
