from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Curtida import Curtida
from api.serializers import CurtidaSerializer

class CurtidaList(APIView):
  def get(self, request):
    pass

  def post(self, request):
    pass

  def put(self):
    pass

  def delete(self):
    pass