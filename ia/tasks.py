from users.models import Documentos
from django.shortcuts import get_object_or_404
from .agents import JuriAI

def ocr_and_markdown_file(instace_id):
  from docling.document_converter import DocumentConverter
  
  documentos = get_object_or_404(Documentos, id=instace_id)
  
  converter = DocumentConverter()
  result = converter.convert(documentos.arquivo.path)
  doc = result.document
  texto = doc.export_to_markdown()
  
  documentos.content = texto
  documentos.save()
  
def rag_documentos(instance_id):
  documentos = get_object_or_404(Documentos, id=instance_id)
  JuriAI.knowledge.insert(
    name=documentos.arquivo.name,
    text_content=documentos.content,
    metadata={
      "cliente_id": documentos.cliente.id,
      "name": documentos.arquivo.name,
    },
  )