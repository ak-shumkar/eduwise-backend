from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    """
    A custom manager that extends django's UserManager
    """
