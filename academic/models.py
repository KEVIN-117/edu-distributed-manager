from django.db import models
from django.forms.fields import UUIDField


# Create your models here.
class Widget(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user_id = models.UUIDField(unique=True, primary_key=True, auto_created=True),
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"UserProfile for user {self.user_id}"