from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    This class defines a user.
    It extends the AbstactUser model
    """
    USER_TYPE = (
        ('client', 'client'),
        ('engineer', 'engineer'),
    )
    email = models.EmailField()
    bio = models.TextField()
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='client')
    avatar = models.ImageField(null=True, default="avatars/default_avatar.svg", upload_to='avatars/')
