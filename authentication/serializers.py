from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "token"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return token


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
