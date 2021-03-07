from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Informations

@receiver(post_delete, sender=Informations)
def delete_user(sender, instance, **kwarags):
    instance.user.delete()