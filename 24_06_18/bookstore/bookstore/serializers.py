from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """
        defines how the class behaves
        we define the configs for the serializer class
        - what model is the data source
        - what data to get from the source
        """
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
        ]
