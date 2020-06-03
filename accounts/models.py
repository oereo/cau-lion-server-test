from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    likenumber = models.CharField(default = "1", max_length = 10)