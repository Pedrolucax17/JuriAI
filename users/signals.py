from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documentos
from ia.tasks import ocr_and_markdown_file

@receiver(post_save, sender=Documentos)
def post_save_documentos(sender, instance, created, **kwargs):
  ocr_and_markdown_file(instace_id= instance.id)