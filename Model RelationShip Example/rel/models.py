from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=200)
    page_description = models.CharField(max_length=200)
    page_views = models.IntegerField()
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_slug = models.CharField(max_length=200)

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=100)
    song_duration = models.IntegerField()

    def get_user(self):
        return " , ".join([str(s) for s in self.user.all()])