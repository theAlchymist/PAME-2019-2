from django.db import models
from django.utils import timezone

class Compartilhamento(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  texto = models.TextField()
  chave_usuario = models.CharField(max_length=20)
  chave_postagem = models.CharField(max_length=20)

  # Relacionamentos
  usuario = models.ManyToManyField(Usuario)
  postagem = models.OneToOneField(Postagem)
  postagem_original = models.ForeignKey(Postagem, on_delete=models.CASCADE)

  def __str__(self):
    return "{} compartilhou {}".format(self.chave_usuario, self.chave_postagem)