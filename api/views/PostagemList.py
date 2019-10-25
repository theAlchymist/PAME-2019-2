from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Postagem import Postagem
from api.serializers import PostagemSerializer

class PostagemList(APIView):
  def get(self, request):
    postagem = Postagem.objects.all()
    data = PostagemSerializer(postagem, many=True).data
    return Response(data)

  def post(self, request):
    # Atribuições
    nome = request.data.usuario['nome']
    texto = request.data['texto']
    chave_usuario = request.data['chave_usuario']
    postagem = Postagem(nome=nome, texto=texto, chave_usuario=chave_usuario)

    # Salva, converte, responde
    postagem.save()
    data = PostagemSerializer(postagem).data
    return Response(data)

  def put(self):
    pass

  def delete(self):
    pass