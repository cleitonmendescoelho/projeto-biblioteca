from django import forms
from .models import UserCadastro
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.hashers import make_password


class UserCadastroForm(forms.ModelForm):

    senha = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        label="Senha"
    )

    class Meta:
        model = UserCadastro
        fields = [
            'nome',
            'sobrenome',
            'data_nascimento',
            'cpf',
            'telefone',
            'email',
            'senha'
        ]

    # -------- Validação personalizada de data --------
    def clean_data_nascimento(self):
        data = self.cleaned_data.get("data_nascimento")
        if data and data > date.today():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
        return data

    # -------- Validação personalizada de CPF --------
    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError("CPF inválido. Use apenas 11 números.")

        return cpf

    # -------- Sobrescrevendo save para hash de senha --------
    def save(self, commit=True):
        user = super().save(commit=False)
        user.senha = make_password(self.cleaned_data["senha"])

        if commit:
            user.save()

        return user