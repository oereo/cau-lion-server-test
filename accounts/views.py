from django.shortcuts import render
from .serializers import RegisterCustomSerializer
from rest_auth.registration.views import RegisterView
from rest_framework import generics
from .models import User
from rest_framework.response import Response

# Create your views here.
class CustomRegistrationsView(RegisterView):
    serializer_class = RegisterCustomSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'Message': 'You have successfully register'}, headers=headers)