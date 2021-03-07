from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    phone =models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
