from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import user_cadastro

def login(request):
    return render(request, 'home/login.html')

def cadastro(request):
    return render(request, 'home/cadastro.html')

def recuperacao_senha(request):
    return render(request, 'home/user_senha.html')

def painel(request):
    return render(request, 'home/index.html')

def criar_cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        data_nasc = request.POST.get("data")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        email =request.POST.get("email")
        senha = make_password(request.POST.get("senha"))
        
        user_cadastro.objects.create(
            nome = nome,
            sobrenome = sobrenome,
            data_nascimento = data_nasc,
            cpf = cpf,
            telefone = telefone,
            email =  email,
            senha = senha
        )
        return redirect('index')
    
    teste = user_cadastro.objects.all()
    return render(request, "home/cadastro.html", {"cadastro": teste}) 

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            # Tenta encontrar o usuário pelo e-mail
            user = user_cadastro.objects.get(email=email)

            # Verifica se a senha digitada bate com o hash salvo
            if check_password(senha, user.senha):
                # Aqui você pode salvar a sessão do usuário
                request.session['usuario_id'] = user.id
                request.session['usuario_nome'] = user.nome
                return redirect('usuario')  # Redireciona para a página inicial
            else:
                return render(request, 'home/admin.html', {'erro': 'Senha incorreta.'})

        except user_cadastro.DoesNotExist:
            return render(request, 'home/admin.html', {'erro': 'Usuário não encontrado.'})

    return render(request, 'home/admin.html')
    
