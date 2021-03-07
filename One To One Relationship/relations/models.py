from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Informations(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT, limit_choices_to={'is_staff':True})
    info = models.CharField(max_length=22)

    def __str__(self):
        return str(self.user)
    