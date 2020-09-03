from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user account info
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'npo')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer that registers a user, using the custon create_user method created in models.py
    """

    #extra password field for validation
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2', 'first_name', 'last_name', 'npo')
        extra_kwargs = {'password': {'write_only': True}}

    #validates password
    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['first_name'],
            validated_data['last_name'],
            validated_data['npo'],
            validated_data['password'],
        )
        return user


class LoginSerializer(serializers.Serializer):
    """
    Login serializer that takes in email and password and returns a user if successful
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Email and/or password")