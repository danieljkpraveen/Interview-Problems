from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)

from .serializers import (
    AuthorSerializer,
    UpdateUserSerializer,
    BookSerializer,
    UpdateBookSerializer
)
from .models import (
    Author,
    Book
)


#######  AUTHOR VIEWS  #######

@api_view(['PUT'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def update_user_and_author(request, pk):
    ## model object
    user = get_object_or_404(User, pk=pk)
    author = get_object_or_404(Author, name=user)
    ## serializer object
    user_serializer = UpdateUserSerializer(user, data=request.data, partial=True)
    author_serializer = AuthorSerializer(author, data=request.data, partial=True)
    ## check validity
    user_valid = user_serializer.is_valid()
    author_valid = author_serializer.is_valid()
    if user_valid and author_valid:
        author.modifed_at = timezone.now()
        author.save()
        user_serializer.save()
        author_serializer.save()
        return Response(
            {
                "user": user_serializer.data,
                "author": author_serializer.data
            }
        )
    else:
        errors = {}
        if not user_valid:
            errors.update(user_serializer.errors)
        if not author_valid:
            errors.update(author_serializer.errors)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def get_authors(request):
    ## model object
    authors = Author.objects.all()
    ## serializer object
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def author_detail(request, pk):
    ## model objects
    user = get_object_or_404(User, pk=pk)
    author = get_object_or_404(Author, name=user)
    ## serializer objects
    serializer = AuthorSerializer(author)
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def delete_author(request, pk):
    ## model objects
    user = get_object_or_404(User, pk=pk)
    author = get_object_or_404(Author, name=user)
    ## update delete flags 
    author.is_deleted = True
    author.deleted_at = timezone.now()
    author.save()
    return Response(
        {"message": "Data deleted"},
        status=status.HTTP_200_OK
    )


#######  BOOK VIEWS #######

@api_view(['POST'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def create_book(request):
    ## POST to create object
    if request.method == 'POST':
        ## serializer object
        serializer = BookSerializer(data=request.data)
        ## check validity
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    ## model object
    book = get_object_or_404(Book, pk=pk)
    ## serializer object
    serializer = UpdateBookSerializer(book, data=request.data, partial=True)
    ## check validity
    serializer_valid = serializer.is_valid()
    if serializer_valid:
        book.modified_at = timezone.now()
        book.save()
        serializer.save()
        return Response({"book": serializer.data})
    else:
        errors = {}
        if not serializer_valid:
            errors.update(serializer.errors)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def get_all_books(request):
    ## model object
    books = Book.objects.all()
    ## serializer object
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def get_book(request, pk):
    ## model object
    book = get_object_or_404(Book, pk=pk)
    ## serializer object
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication
])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    ## model object
    book = get_object_or_404(Book, pk=pk)
    ## set delete flags
    book.is_deleted = True
    book.deleted_at = timezone.now()
    book.save()
    return Response(
        {"message": "Data deleted"},
        status=status.HTTP_200_OK
    )
