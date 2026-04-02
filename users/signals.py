from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documentos

@receiver(post_save, sender=Documentos)
def post_save_documentos(sender, instance, created, **kwargs):
  pass