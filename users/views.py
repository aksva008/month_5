from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserCreateSerializer,
    ConfirmUserSerializer,
    UserAuthSerializer
)
from .models import ConfirmCode


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    return Response(
        {"user_id": user.id},
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = ConfirmUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    code = serializer.validated_data['code']

    try:
        user = User.objects.get(username=username)
        confirm = ConfirmCode.objects.get(user=user)

        if confirm.code != code:
            return Response(
                {"error": "Incorrect code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.is_active = True
        user.save()
        confirm.delete()

        return Response({"message": "User confirmed!"})

    except User.DoesNotExist:
        return Response(
            {"error": "User not found"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(
        username=serializer.validated_data['username'],
        password=serializer.validated_data['password']
    )

    if not user:
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not user.is_active:
        return Response(
            {"error": "User not confirmed"},
            status=status.HTTP_403_FORBIDDEN
        )

    refresh = RefreshToken.for_user(user)

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    })
