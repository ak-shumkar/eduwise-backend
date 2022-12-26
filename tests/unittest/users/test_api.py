import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from eduwise.users.models import AGENT, STUDENT

User = get_user_model()

client = APIClient()


@pytest.mark.django_db
def test_student_register():
    response = client.post('/api/auth/users/', data={'username': 'demouser', 'password': 'demopassword'})
    assert response.status_code == 201
    assert response.data['role'] == STUDENT


@pytest.mark.django_db
def test_agent_register():
    response = client.post('/api/auth/users/', data={'username': 'demoagent',
                                                     'password': 'demopassword',
                                                     'role': AGENT})
    assert response.status_code == 201
    assert response.data['role'] == AGENT


@pytest.mark.django_db
def test_users_me(user_access_token, user):
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_access_token)
    response = client.get('/api/auth/users/me/')
    assert response.status_code == 200
    assert response.json()['username'] == user.username
