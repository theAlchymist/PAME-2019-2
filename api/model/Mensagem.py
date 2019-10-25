from django.db import models
from django.utils import timezone

class Mensagem(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  texto = models.TextField()
  chave_remetente = models.CharField(max_length=20)
  chave_destinatario = models.CharField(max_length=20)

  # Relacionamentos
  remetente = models.ForeignKey('api.Usuario', on_delete=models.CASCADE)
  destinatario = models.ForeignKey('api.Usuario', on_delete=models.CASCADE)

  def __str__(self):
    return self.texto