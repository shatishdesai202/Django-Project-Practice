from django.db import models
from .managers import CustomManager
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    rno = models.IntegerField()
    objects = models.Manager()
    abc = CustomManager() 
    rng = CustomManager()
    reverse = CustomManager()


class ProxyStudent(Student):
    reverse = CustomManager()
    class Meta:
        proxy = True