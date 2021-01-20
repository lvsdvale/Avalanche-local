from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Cadastro(UserCreationForm):
    class Meta:
        model = user
        fields = ('email', 'name', 'CPF','Genero','Data','Curso','Registro_Academico','Telefone', 'password1', 'password2', )


class Reset(forms.Form):
    Email = forms.EmailField(max_length=255,help_text='Digite seu email',label = "Email",label_suffix = "Email")
    CPF = forms.CharField(max_length=255,help_text= 'Digite seu CPF',label = "CPF",label_suffix = "CPF")
