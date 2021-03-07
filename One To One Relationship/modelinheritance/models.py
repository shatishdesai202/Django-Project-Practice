from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)

class Like(Page):
    user_liked = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True)
    likes = models.IntegerField()
