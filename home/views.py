from .models import MinhaBiblioteca
from .models import UserCadastro
from .models import Livro
from .forms import UserCadastroForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # Biblioteca para mensagens de erros de validação
from django.core.exceptions import ValidationError # Biblioteca para erros de excessões de validação
from datetime import date # Biblioteca para validação de datas
from django.core.validators import validate_email # Biblioteca para validação de emails
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    return render(request, 'home/user/login.html')

def verificar_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        try:
            # Tenta encontrar o usuário pelo e-mail
            user = UserCadastro.objects.get(email=email)

            # Verifica se a senha digitada bate com o hash salvo
            if check_password(senha, user.senha):
                # Gerenciamento de seções do usuário
                # request.session['usuario_id'] = user.id
                # request.session['usuario_nome'] = user.nome
                return redirect('acesso_painel')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Email ou senha incorretos')
                return redirect('login')

        except UserCadastro.DoesNotExist:
            messages.error(request, 'Usuário não cadastrado')
            return redirect('login')

def formulario_cadastro(request):
    return render(request, 'home/user/cadastro.html')

def cadastrar_usuario(request):

    if request.method == "POST":
        form = UserCadastroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("cadastrar_usuario")

    else:
        form = UserCadastroForm()

    return render(
        request,
        "home/user/cadastro.html",
        {"form": form}
    )

def recuperacao_senha(request):
    return render(request, 'home/user/rec_senha.html')

def acesso_painel(request):
    dados = Livro.objects.all().order_by('-ordem')
    return render(request, 'home/paginas/index.html', {'dados':dados})

def biblioteca_pessoal(request):
    dados = MinhaBiblioteca.objects.all()
    return render(request, 'home/paginas/biblioteca.html', {'dados': dados})


def adicionar_biblioteca(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if not MinhaBiblioteca.objects.filter(id_livro=livro).exists():

        MinhaBiblioteca.objects.create(
            id_livro=livro,
            nome=livro.nome,
            imagem_capa=livro.livro_imagem
        )

    return redirect('biblioteca_pessoal')


def historico(request):
    return render(request, 'home/paginas/historico.html')

def relatorios(request):
    return render(request, 'home/sections/relatorios.html')


        
        


