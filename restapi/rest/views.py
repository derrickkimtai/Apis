from django.shortcuts import render
from rest_framework import viewsets
from .models import Name
from .serializers import NameSeralizer

class NameView(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSeralizer
