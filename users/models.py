from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    profile_picture = models.URLField()
    bio = models.CharField(max_length=255)
