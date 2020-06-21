from django import forms
from .models import inscricao_Campanhas, inscricao_modalidades, inscricao_games,processo_seletivo,contatos


class Form_inscricao_campanhas(forms.ModelForm):
    class Meta:
        model = inscricao_Campanhas
        fields = ['name','email','CPF','Curso','Ra','Campanha','local','Telefone','tag']

class Form_incricao_esportes(forms.ModelForm):
    class Meta:
        model = inscricao_modalidades
        fields = ['usuario','modalidade']
class Form_inscricao_games(forms.ModelForm):
    class Meta:
        model = inscricao_games
        fields = ['name','Curso','Ra','Game','Telefone','tag']
class Form_inscricao_processo_seletivo(forms.ModelForm):
    class Meta:
        model = processo_seletivo
        fields = ['name','email','Areas','Curso','Ra','Telefone']
class Form_contatos(forms.ModelForm):
    class Meta:
        model = contatos
        fields = ['name','email','assunto','mensagem']