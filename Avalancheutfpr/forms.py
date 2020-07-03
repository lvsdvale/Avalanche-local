from django import forms
from .models import *


class Form_inscricao_campanhas(forms.ModelForm):
    class Meta:
        model = inscricao_campanhas_sociais
        fields = ['usuario','campanha',]

class Form_incricao_esportes(forms.ModelForm):
    class Meta:
        model = inscricao_modalidades
        fields = ['usuario','modalidade']
class Form_inscricao_games(forms.ModelForm):
    class Meta:
        model = inscricao_E_sports
        fields = ['usuario','game']

class Form_contatos(forms.ModelForm):
    class Meta:
        model = contatos
        fields = ['name','email','assunto','mensagem']