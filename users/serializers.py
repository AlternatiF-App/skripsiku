from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class GetUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'teacher_class', 'is_active']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'teacher_class']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100, read_only=True)
    password = serializers.CharField(max_length=68, min_length=5, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email','username', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
        if not user.is_active:
            raise serializers.ValidationError('User not active, please contact admin')
        if not user:
            raise serializers.ValidationError('Invalid users, try again')
        return {
            'id':user.id,
            'email':user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')