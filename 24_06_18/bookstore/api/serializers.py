from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Author,
    Book
)


######  AUTHOR SERIALIZERS  ######
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'biography',]


class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


######  BOOK SERIALIZERS  ######

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn',]


class UpdateBookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    published_date = serializers.DateTimeField(required=False)
    isbn = serializers.CharField(required=False)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance
