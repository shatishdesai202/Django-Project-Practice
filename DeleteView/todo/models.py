from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    