import pytest
import unittest
import random
from users.djoser import serializers
from users.models import User


@pytest.mark.django_db
class TestUserRegistrationSerializer(unittest.TestCase):
    def setUp(self) -> None:
        self.register_data = {
            'username': "test_username",
            'password': "test_password",
            'first_name': "John",
            'last_name': "Legend",
            'email': "johnlegend@gmail.com",
            'role': "A"
        }
        # self.user = User.objects.create(**self.register_data)
        self.serializer = serializers.UserRegistrationSerializer(self.register_data)
        # print(self.serializer.fields)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), {'username', 'first_name', 'last_name', 'email', 'role'})

    def test_fields_content(self):
        data = self.serializer.data
        for k, v in self.register_data.items():
            if k != 'password':
                self.assertEqual(data[k], v)

    def test_short_password(self):
        self.register_data['password'] = 'A78dhrw'
        serializer = serializers.UserRegistrationSerializer(data=self.register_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'password'})

    def test_long_password(self):
        self.register_data['password'] = "".join(chr(random.randint(1, 128)) for _ in range(129))
        serializer = serializers.UserRegistrationSerializer(data=self.register_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'password'})

    def test_username_uniqueness(self):
        User.objects.create(**self.register_data)
        serializer = serializers.UserRegistrationSerializer(data=self.register_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'username'})

    def test_long_username(self):
        self.register_data['username'] = "".join(chr(random.randint(1, 128)) for _ in range(129))
        serializer = serializers.UserRegistrationSerializer(data=self.register_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {'username'})


@pytest.mark.django_db
class TestUserDetailsSerializer(unittest.TestCase):
    def setUp(self) -> None:
        self.register_data = {
            'username': "test_username",
            'password': "test_password",
            'first_name': "John",
            'last_name': "Legend",
            'email': "johnlegend@gmail.com",
            'role': "A"
        }
        self.user = User.objects.create(**self.register_data)
        self.serializer = serializers.UserDetailsSerializer(self.user)

    def test_get_contains_expected_fields(self):
        data = self.serializer.data
        print(data.keys())
        fields = {f.name for f in User._meta.fields}.difference({'password'})
        self.assertCountEqual(data.keys(), fields)

    def test_read_only_fields(self):
        read_only_fields = ['last_login', 'is_staff', 'id', 'role', 'is_active', 'date_joined', 'is_superuser']
        serializer = serializers.UserDetailsSerializer(data={'id': 1})
        serializer.is_valid()
        print(serializer.errors)
        assert False
        # for read_only_field in read_only_fields:
        #     with pytest.raises()
        # data = self.serializer.data
        # print(data.keys())
        # fields = {f.name for f in User._meta.fields}.difference({'password'})
        # self.assertCountEqual(data.keys(), fields)
