from django import forms
from .models import *


class Form_contatos(forms.ModelForm):
    class Meta:
        model = contatos
        fields = ['name','email','assunto','mensagem']