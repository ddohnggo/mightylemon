from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Not everyone is Brian Rosner.
    """
    user = models.ForeignKey(User, unique=True)

    full_name = models.CharField(max_length=60, blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    about_me = models.TextField(blank=True)