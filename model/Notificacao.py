from django.db import models
from django.utils import timezone
from api.model.Comentario import Comentario
from api.model.Compartilhamento import Compartilhamento
from api.model.Curtida import Curtida
from api.model.Mensagem import Mensagem
from api.model.Postagem import Postagem

class Notificacao(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  acao = models.CharField(max_length=20)
  chave_remetente = models.CharField(max_length=20)
  chave_destinatario = models.CharField(max_length=20)

  # Relacionamentos
  comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
  compartilhamento = models.ForeignKey(Compartilhamento, on_delete=models.CASCADE)
  curtida = models.ForeignKey(Curtida, on_delete=models.CASCADE)
  mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE)
  postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

  def __str__(self):
    return "{} - {} - {}".format(self.chave_remetente, self.acao, self.chave_destinatario)