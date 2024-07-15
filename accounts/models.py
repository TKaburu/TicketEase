from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    This class defines a user.
    It extends the AbstactUser model
    """
    email = models.EmailField()
    bio = models.TextField()
    avatar = models.ImageField(null=True, default="avatars/default_avatar.svg", upload_to='avatars/')
