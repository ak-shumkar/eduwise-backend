import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
@pytest.fixture
def student():
    student = User.objects.create_user(username="student@config.com", password="super_secret")
    return student


@pytest.mark.django_db
@pytest.fixture
def agent():
    agent = User.objects.create_user(username="agent@config.com", password="super_secret", role="A")
    return agent
