from django.contrib.auth.models import User
from .models import Livro
from .models import MinhaBiblioteca
from .models import Historico
from .forms import UserCadastroForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # Biblioteca para mensagens de erros de validação
from django.core.exceptions import ValidationError # Biblioteca para erros de excessões de validação
from datetime import date
from django.core.validators import validate_email 
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('acesso_painel')
    
    return render(request, 'home/user/login.html')

def verificar_login(request):
    if request.method != 'POST':
        return redirect('login')
        
        
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    usuario = User.objects.filter(email=email).first()
    
    user = authenticate(
        request,
        username=usuario.username if usuario else None,
        password=senha
    )
    if user is not None:
        login(request,user)
        return redirect('acesso_painel')

    messages.error(request, 'Usuario ou senha invalidos')
    return redirect('login')

def formulario_cadastro(request):
    return render(request, 'home/user/cadastro.html')

def cadastrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('acesso_painel')

    if request.method == "POST":
        form = UserCadastroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
    else:
        form = UserCadastroForm()

    return render(request, 'home/user/cadastro.html', {'form': form})

def recuperacao_senha(request):
    return render(request, 'home/user/rec_senha.html')

@login_required
def acesso_painel(request):
    dados = Livro.objects.all().order_by('-ordem')
    return render(request, 'home/paginas/index.html', {'dados':dados})

@login_required
def biblioteca_pessoal(request):
    dados = MinhaBiblioteca.objects.all()
    return render(request, 'home/paginas/biblioteca.html', {'dados': dados})

@login_required
def adicionar_biblioteca(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if not MinhaBiblioteca.objects.filter(id_livro=livro).exists():

        MinhaBiblioteca.objects.create(
            usuario=request.user,
            id_livro=livro,
            nome=livro.nome,
            imagem_capa=livro.livro_imagem
        )

        Historico.objects.create(
            usuario=request.user,
            nome_livro=livro.nome,
            autor=livro.autor,
            paginas=livro.pagina_livro,
            data=date.today()
        )

    return redirect('biblioteca_pessoal')

@login_required
def remover_livro(request,livro_id):
    livro = get_object_or_404(
        MinhaBiblioteca,
        id=livro_id,
        usuario=request.user
    )
    livro.delete()
    return redirect('biblioteca_pessoal')

@login_required
def painel_historico(request):
    livros = Historico.objects.all()
    return render(request, 'home/paginas/historico.html', {'livros': livros})  

@login_required
def relatorios(request):
    return render(request, 'home/sections/relatorios.html')

def sair(request):
    logout(request)
    return redirect('login')


        
        


