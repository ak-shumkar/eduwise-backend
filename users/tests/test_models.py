import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def test_student():
    student = User(username='alipay', password='secret')
    print(student)
    print(student.__class__.__mro__)
    return student

