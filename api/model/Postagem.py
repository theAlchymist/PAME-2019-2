from django.db import models
from django.utils import timezone

class Postagem(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  texto = models.TextField()
  # imagem = models.ImageField()
  # comentarios = 
  # curtidas = 
  # compartilhamentos =
  chave_usuario = models.CharField(max_length=20)
  chave_usuario_original = models.CharField(max_length=20)
  chave_postagem = models.CharField(max_length=20)

  # Relacionamentos
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

  def __str__(self):
    return self.chave_postagem