from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
class Cadastro(UserCreationForm):
    class Meta:
        model = user
        fields = ('email', 'Nome_completo', 'CPF', 'Curso','Registro_Academico','Telefone', 'password1', 'password2', )


class Reset(forms.Form):
    email = forms.EmailField(max_length=255,help_text='Digite seu email')
    cpf = forms.CharField(max_length=255,help_text= 'Digite seu CPF')
