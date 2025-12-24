from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_premium',
            'timezone',
            'locale',
            'date_joined',
        ]
        read_only_fields = ['id', 'is_premium', 'date_joined']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
            'timezone',
            'locale',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username') or email
        validated_data['username'] = username
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

