from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer


User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    password = serializers.CharField(style={"input_type": "password"},
                                     write_only=True,
                                     max_length=128)

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'role']


class UserDetailsSerializer(DjoserUserSerializer):

    class Meta(DjoserUserSerializer.Meta):
        fields = ['username', 'id', 'first_name', 'last_name', 'email'] + \
                 ['last_login', 'is_staff', 'id', 'role', 'is_active', 'date_joined', 'is_superuser',
                  'middle_name', 'gender', 'birthdate', 'country', 'phone', 'education_level', 'motivation']
        read_only_fields = ['last_login', 'is_staff', 'id', 'role', 'is_active', 'date_joined', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['role']
