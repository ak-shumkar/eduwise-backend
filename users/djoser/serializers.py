from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import User

from django import forms
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'role']


class UserDetailsSerializer(DjoserUserSerializer):

    class Meta(DjoserUserSerializer.Meta):
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailsGetSerializer(DjoserUserSerializer):
    role_text = serializers.ReadOnlyField(source='get_role_display')

    class Meta(DjoserUserSerializer.Meta):
        fields = '__all__'
        read_only_fields = ['role_text']
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ("username", "email", "password",)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['role']


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
