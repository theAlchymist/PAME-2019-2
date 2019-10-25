from django.db import models
from django.utils import timezone

class Curtida(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  chave_usuario = models.CharField(max_length=20)
  chave_entidade = models.CharField(max_length=20)

  # Relacionamentos
  usuario = models.ForeignKey('api.Usuario', on_delete=models.CASCADE)
  comentario = models.ForeignKey('api.Comentario', on_delete=models.CASCADE)
  postagem = models.ForeignKey('api.Postagem', on_delete=models.CASCADE)

  def __str__(self):
    return "{} curtiu {}".format(self.chave_usuario, self.chave_entidade)