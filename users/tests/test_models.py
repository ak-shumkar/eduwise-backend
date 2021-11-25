import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def student():
    student = User(username='student', password='secret')
    return student


@pytest.fixture
def agent():
    agent = User(username='agent', password='secret', role='A')
    return agent


@pytest.mark.django_db
def test_create_default_user():
    user = User(username="alex", password='secret')
    user.full_clean()
    user.save()
    db_user = User.objects.all()[0]
    assert db_user is not None
    assert db_user.is_student
    assert not db_user.is_agent
    assert not db_user.is_staff

    # default fields
    assert db_user.date_joined is not None
    assert db_user.is_active


def test_is_student(student):
    assert student.is_student


def test_is_agent(agent):
    assert agent.is_agent
