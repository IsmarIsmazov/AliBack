from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(min_length=6)
    phone_number = PhoneNumberField(region="KG")
    last_name = serializers.CharField(min_length=6)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'avatar_photo', 'phone_number']
        read_only_fields = ['email', 'phone_number']
