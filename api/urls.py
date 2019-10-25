from django.urls import path
from api.views import ComentarioList, CompartilhamentoList, CurtidaList, MensagemList, NotificacaoList, PostagemList, UsuarioList

urlpatterns = [
    path('comentario/', ComentarioList.as_view()),
    path('compartilhamento/', CompartilhamentoList.as_view()),
    path('curtida/', CurtidaList.as_view()),
    path('mensagem/', MensagemList.as_view()),
    path('notificacao/', NotificacaoList.as_view()),
    path('postagem/', PostagemList.as_view()),
    path('usuario/', UsuarioList.as_view()),
]