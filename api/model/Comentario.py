from django.db import models
from django.utils import timezone
from api.model.Usuario import Usuario
from api.model.Postagem import Postagem

class Comentario(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  texto = models.TextField()
  chave_usuario = models.CharField(max_length=20)
  chave_postagem = models.CharField(max_length=20)

  # Relacionamentos
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

  def __str__(self):
    return "{} comentou {}".format(self.chave_usuario, self.chave_postagem)