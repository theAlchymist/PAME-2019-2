from rest_framework import serializers
from api.model.Comentario import Comentario
from api.model.Compartilhamento import Compartilhamento
from api.model.Curtida import Curtida
from api.model.Mensagem import Mensagem
from api.model.Notificacao import Notificacao
from api.model.Postagem import Postagem
from api.model.Usuario import Usuario

class ComentarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comentario
    fields  = '__all__'

class CompartilhamentoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Compartilhamento
    fields  = '__all__'

class CurtidaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curtida
    fields  = '__all__'

class MensagemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mensagem
    fields  = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notificacao
    fields  = '__all__'

class PostagemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Postagem
    fields  = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields  = '__all__'