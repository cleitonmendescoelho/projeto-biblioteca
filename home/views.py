from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import UserCadastro

def login(request):
    return render(request, 'home/user/login.html')

def cadastrar_usuario(request):
    return render(request, 'home/user/cadastro.html')

def recuperacao_senha(request):
    return render(request, 'home/user/rec_senha.html')

def acesso_painel(request):
    return render(request, 'home/index.html')

def historico(request):
    return render(request, 'home/sections/historico.html')

def criar_cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        data_nasc = request.POST.get("data")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        email =request.POST.get("email")
        senha = make_password(request.POST.get("senha"))
        
        UserCadastro.objects.create(
            nome = nome,
            sobrenome = sobrenome,
            data_nascimento = data_nasc,
            cpf = cpf,
            telefone = telefone,
            email =  email,
            senha = senha
        )
        return redirect('login')
    
    teste = UserCadastro.objects.all()
    return render(request, "home/user/cadastro.html", {"cadastro": teste}) 

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
                return render(request, 'home/user/login.html', {'erro': 'Senha incorreta.'})

        except UserCadastro.DoesNotExist:
            return render(request, 'home/user/login.html', {'erro': 'Usuário não encontrado.'})

    return render(request, 'home/index.html')
    
