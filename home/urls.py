from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('senha', views.recuperacao_senha, name='recuperacao_senha'),
    path('painel', views.acesso_painel, name='acesso_painel'),
    path('usuarios/novo', views.criar_cadastro, name='criar_cadastro'),
    path('login', views.verificar_login, name='verificar_login'),
    path('historico', views.historico, name='historico'),
    path('bilioteca', views.biblioteca_pessoal, name = 'biblioteca_pessoal'),
    path('dados', views.relatorios, name='relatorios')
]