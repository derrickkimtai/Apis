from rest_framework import serializers
from .models import Name
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class NameSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'middle_name', 'last_name', 'phone')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Password entered does not match "})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
        )

        user.set_password(validated_data['password']) #hash the password
        user.save()

        return user