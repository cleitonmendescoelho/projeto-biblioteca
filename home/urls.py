from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.verificar_login, name='verificar_login'),
    path('cadastro', views.formulario_cadastro, name='formulario_cadastro'),
    path('usuarios/novo', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('senha', views.recuperacao_senha, name='recuperacao_senha'),
    path('painel', views.acesso_painel, name='acesso_painel'),
    path('bilioteca/', views.biblioteca_pessoal, name = 'biblioteca_pessoal'),
    path('historico', views.historico, name='historico'),
    path('dados', views.relatorios, name='relatorios'),
    path('adicionar-biblioteca/<int:livro_id>/', views.adicionar_biblioteca, name='adicionar_biblioteca'),
]