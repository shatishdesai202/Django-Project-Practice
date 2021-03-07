from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    singer = models.ManyToManyField(User)
    name = models.CharField(max_length=20)
    length = models.IntegerField()

    def all_singer(self):
        return " / ".join([str(s) for s in self.singer.all()])


