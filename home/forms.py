from django.contrib.auth.models import User
from .models import UserCadastro
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django import forms
from django.db import transaction


class UserCadastroForm(UserCreationForm):
    
    first_name = forms.CharField(
        max_length=255,
        min_length=2,
        label='Nome'
    )
    
    last_name = forms.CharField(
        max_length=255,
        min_length=2,
        label='Sobrenome'
    )
    
    email = forms.EmailField(label='Email')
    
    data_nascimento = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    cpf = forms.CharField(max_length=11, min_length=11, label='CPF')
    
    telefone = forms.CharField(max_length=15, min_length=10, label='Telefone')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ja esta cadastrado.')

        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '')

        if not cpf.isdigit():
            raise forms.ValidationError('CPF invalido. Use apenas numeros.')

        if UserCadastro.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF ja esta cadastrado.')

        return cpf

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')

        if data_nascimento and data_nascimento > date.today():
            raise forms.ValidationError('A data de nascimento nao pode ser no futuro.')

        return data_nascimento

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            UserCadastro.objects.create(
                usuario=user,
                data_nascimento=self.cleaned_data['data_nascimento'],
                cpf=self.cleaned_data['cpf'],
                telefone=self.cleaned_data['telefone']
            )

        return user
