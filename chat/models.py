from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_moderator = models.BooleanField(default=False)

class Channel(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(CustomUser)

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
