from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import User

class RegisterCustomSerializer(RegisterSerializer):
    #first_name = serializers.CharField(required=True)
    #last_name = serializers.CharField(required=True)
    likelion_number = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def custom_signup(self, request, user):
    #     return{
    #         'likelion_number' : self.validated_data.get('likelion_number', '')
    #     }
         user.likelion_number = self.validated_data.get('likelion_number', '')
         user.phone_number = self.validated_data.get('phone_number','')
         user.save(update_fields=['likelion_number', 'phone_number'])
    
    class Meta:
        model = User
        write_only_fields = 'password'
        read_only_fields = 'id'
        fields = ('id',
              'username',
              'email',
              'password',
              'likelion_number',
            )

        