from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    likelion_number = models.CharField(default = "1", max_length = 10)
    phone_number = models.CharField(default='1', max_length = 12)