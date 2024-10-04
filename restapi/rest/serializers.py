from rest_framework import serializers
from .models import Name, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class NameSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'


from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone']

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user