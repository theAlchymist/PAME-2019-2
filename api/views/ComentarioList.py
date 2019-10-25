from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Comentario import Comentario
from api.serializers import ComentarioSerializer

class ComentarioList(APIView):
  def get(self, request):
    pass

  def post(self, request):
    pass

  def put(self):
    pass

  def delete(self):
    pass