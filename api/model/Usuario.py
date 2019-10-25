from django.db import models
from api.model.Notificacao import Notificacao

class Usuario(models.Model):
  # Atributos
  email = models.EmailField(max_length=254)
  senha = models.CharField(max_length=20)
  nome = models.CharField(max_length=20)
  chave_usuario = models.CharField(max_length=20)
  # foto = models.ImageField()

  # Relacionamentos
  notificacao = models.ManyToManyField(Notificacao)
  
  def __str__(self):
    return self.chave_usuario