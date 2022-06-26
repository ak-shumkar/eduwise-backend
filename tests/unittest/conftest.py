import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def admin_user_credentials():
    return {}


@pytest.fixture
def client():
    return APIClient()


# @pytest.fixture
# def admin_client(admin_user_credentials):
#     admin_credentials = {"username": "admin", "password": "admin-secret"}
#     User.objects.create_super_user(**admin_credentials)
#     client = Client()
#     client.login(**admin_user_credentials)
#
#     return client
