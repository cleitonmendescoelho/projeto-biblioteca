from django.db import models
from django.contrib.auth.models import User

class UserCadastro(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique = True)
    telefone = models.CharField(max_length=15)

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
    
class MinhaBiblioteca(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='biblioteca_usuario',
        null=True,
        blank=True
    )
    
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120)
    imagem_capa = models.CharField(max_length=255)
    
class Historico(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='historico_usuario',
        null=True,
        blank=True
    )
    
    nome_livro = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    paginas = models.PositiveIntegerField()
    data = models.DateField()
    