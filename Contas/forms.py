from .models import *
from django.contrib.auth.forms import UserCreationForm
class Cadastro(UserCreationForm):
    class Meta:
        model = user
        fields = ('email', 'Nome_completo', 'CPF', 'Curso','Registro_Academico','Telefone', 'password1', 'password2', )