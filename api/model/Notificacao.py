from django.db import models
from django.utils import timezone

class Notificacao(models.Model):
  # Atributos
  data_criada = models.DateTimeField(default=timezone.now)
  acao = models.CharField(max_length=20)
  chave_remetente = models.CharField(max_length=20)
  chave_destinatario = models.CharField(max_length=20)

  # Relacionamentos
  comentario = models.ForeignKey('api.Comentario', on_delete=models.CASCADE)
  compartilhamento = models.ForeignKey('api.Compartilhamento', on_delete=models.CASCADE)
  curtida = models.ForeignKey('api.Curtida', on_delete=models.CASCADE)
  mensagem = models.ForeignKey('api.Mensagem', on_delete=models.CASCADE)
  postagem = models.ForeignKey('api.Postagem', on_delete=models.CASCADE)

  def __str__(self):
    return "{} - {} - {}".format(self.chave_remetente, self.acao, self.chave_destinatario)