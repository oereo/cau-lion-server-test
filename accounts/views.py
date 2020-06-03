from django.shortcuts import render
from .serializers import RegisterCustomSerializer
from rest_framework import generics

# Create your views here.
class CustomRegistrationsView(generics.GenericAPIView):
    serializer_class = RegisterCustomSerializer