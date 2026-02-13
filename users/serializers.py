from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConfirmCode
import random


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("User already exists!")
        return username

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data,
            is_active=False
        )

        code = str(random.randint(100000, 999999))
        ConfirmCode.objects.create(user=user, code=code)

        print("CONFIRM CODE:", code)  

        return user


class ConfirmUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
