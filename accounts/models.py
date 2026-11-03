from django.db import models

from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    phone = models.CharField(max_length=100,unique=True)
