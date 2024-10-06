from rest_framework import serializers
from .models import Login, Name, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class NameSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'


from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2',  'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        return attrs
    

    def create(self, validated_data):

        validated_data.pop('password2')

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

        def __str__(self):
            return self.username