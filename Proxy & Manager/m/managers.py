from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    
    def get_abcd(self, r1,r2):
        return super().get_queryset() .filter(rno__range=(r1,r2))
    
    def reverse(self):
        return super().get_queryset().order_by('-name')

    def rangerID(self, r1,r2):
        return super().get_queryset() .filter(rno__range=(r1,r2)).order_by('-id')

