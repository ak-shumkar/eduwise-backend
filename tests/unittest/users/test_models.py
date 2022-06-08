import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


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


@pytest.mark.django_db
def test_is_student(student):
    assert student.is_student


@pytest.mark.django_db
def test_is_agent(agent):
    assert agent.is_agent
