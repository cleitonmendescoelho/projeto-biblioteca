from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('senha', views.recuperacao_senha, name='senha'),
    path('painel', views.painel, name='painel'),
    path('user-cadastro', views.criar_cadastro, name='user-cadastro'),
    path('login', views.user_login, name='user-login'),
]