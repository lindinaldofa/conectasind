from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Seu e-mail ou CPF",
                "class": "form-control"
            }
        ),
        label='E-mail ou CPF')
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ),
        label='Senha')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Primeiro Nome",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        label="Sobrenome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Seu e-mail",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ),
        label='Senha')
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme a Senha",
                "class": "form-control"
            }
        ),
        label='Confirmação de Senha')

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')