from django.shortcuts import render
from rest_framework.views import  APIView
from .models import Name, CustomUser
from .serializers import NameSeralizer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSeralizer

from rest_framework import generics
from .serializers import CustomUserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer