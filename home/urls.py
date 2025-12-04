from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('senha', views.recuperacao_senha, name='senha'),
    path('painel', views.painel, name='painel'),
    path('', views.criar_cadastro, name='cadastro'),
    path('login', views.user_login, name='login'),
]