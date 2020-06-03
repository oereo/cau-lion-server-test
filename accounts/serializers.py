from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

class RegisterCustomSerializer(RegisterSerializer):

    class Meta:
        model = User
        