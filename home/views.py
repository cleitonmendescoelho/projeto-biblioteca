from .models import UserCadastro
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages # Biblioteca para mensagens de erros de validação
from django.core.exceptions import ValidationError # Biblioteca para erros de excessões de validação
from datetime import date # Biblioteca para validação de datas
from django.core.validators import validate_email # Biblioteca para validação de emails
from django.contrib.auth.hashers import make_password, check_password

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
        nome = request.POST.get("nome", "").strip()
        sobrenome = request.POST.get("sobrenome", "").strip()
        data_nasc = request.POST.get("data")
        cpf = request.POST.get("cpf", "").strip()
        telefone = request.POST.get("telefone", "").strip()
        email = request.POST.get("email", "").strip()
        senha_raw = request.POST.get("senha", "")

        erros = []

        # ---------- Validações ----------
        if not nome or len(nome) < 3:
            erros.append("O nome é obrigatório e deve ter no mínimo 3 caracteres.")

        if not sobrenome:
            erros.append("O sobrenome é obrigatório.")

        if not data_nasc:
            erros.append("A data de nascimento é obrigatória.")
        else:
            if date.fromisoformat(data_nasc) > date.today():
                erros.append("A data de nascimento não pode ser no futuro.")

        if not cpf or len(cpf) != 11 or not cpf.isdigit():
            erros.append("CPF inválido. Use apenas números (11 dígitos).")

        if not telefone or len(telefone) < 10:
            erros.append("Telefone inválido.")

        try:
            validate_email(email)
        except ValidationError:
            erros.append("E-mail inválido.")

        if UserCadastro.objects.filter(email=email).exists():
            erros.append("Este e-mail já está cadastrado.")

        if len(senha_raw) < 8:
            erros.append("A senha deve ter no mínimo 8 caracteres.")

        # ---------- Se houver erro - Envio para o template ----------
        if erros:
            for erro in erros:
                messages.error(request, erro)

            return render(request, "home/user/cadastro.html", {
                "dados": request.POST
            })

        # ---------- Criação segura ----------
        UserCadastro.objects.create(
            nome=nome,
            sobrenome=sobrenome,
            data_nascimento=data_nasc,
            cpf=cpf,
            telefone=telefone,
            email=email,
            senha=make_password(senha_raw)
        )

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("cadastrar_usuario")

    return render(request, "home/user/cadastro.html") 

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

