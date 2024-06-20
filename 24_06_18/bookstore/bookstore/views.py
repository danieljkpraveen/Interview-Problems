from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from api.models import Author


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    ##
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(instance=user)
    ##
    if not user.check_password(password): # if password doesn't match
        return Response(
            {"detail": "Not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    token, created = Token.objects.get_or_create(user=user)
    ##
    return Response(
        {
            "token": token.key,
            "user": serializer.data
        }
    )


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    ##
    if serializer.is_valid():
        serializer.save()
        username = request.data['username']
        password = request.data['password']
        user = get_object_or_404(User, username=username)
        user.set_password(password)
        user.save()
        author = Author.objects.create(
            name=user,
        )
        author.save()
        token = Token.objects.create(user=user)
        return Response(
            {
                "token": token.key,
                "user": serializer.data
            }
        )
    ##
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
@authentication_classes([
    SessionAuthentication,  # enables auth using session id
    TokenAuthentication  # enables auth using token
])
@permission_classes([IsAuthenticated])
def test_token(request):
    ##
    return Response(f"passed for {request.user.email}")
