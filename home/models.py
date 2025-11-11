from django.db import models

class user_cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=128)
