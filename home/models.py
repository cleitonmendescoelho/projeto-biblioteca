from django.db import models

class UserCadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique = True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=128)

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=255)
    autor= models.CharField(max_length=120)
    genero = models.CharField(max_length=120)
    editora = models.CharField(max_length=120)
    pagina_livro = models.PositiveIntegerField()
    data_publicação = models.DateField()
    livro_imagem = models.CharField(max_length=255, null=True, blank=True)
    ordem = models.IntegerField(default=0)
    