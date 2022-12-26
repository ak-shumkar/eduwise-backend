import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
@pytest.fixture
def user():
    user = User(username='test_user')
    user.set_password("test_password")
    user.save()
    return user


@pytest.fixture
def admin_user_credentials():
    return {}


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_access_token(client, user):
    client = APIClient()
    response = client.post("/api/auth/jwt/create/", data={"username": "test_user", "password": "test_password"})
    return response.json()["access"]
