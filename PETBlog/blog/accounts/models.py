from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    """

    Advanced user model(CustomUser) with roles.

    """
    ROLE_CHOICES = [
        ('user', 'User (Default)'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

def __str__(self):
        return self.username
