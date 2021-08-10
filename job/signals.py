from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Jobs

@receiver(pre_save, sender=Jobs)
def assign_user(sender, instance, *args, **kwargs): #looks for current instance
    pass