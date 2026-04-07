from django.db import models
from users.models import Cliente

class Pergunta(models.Model):
    pergunta = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.pergunta
