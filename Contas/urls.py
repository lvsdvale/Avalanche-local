from django.urls import path
from .views import *
urlpatterns = [
    path('Cadastro/', Cadastrar_usuarios,name = 'Cadastro'),
    path('Login/',Login,name = 'Login'),
    path('MinhaConta/',Minha_Conta,name = 'Minha_Conta'),
    path('MeusDados/',Meus_Dados,name = 'Meus_Dados'),
    path('ResetarSenha/',Resetar,name = 'Resetar_Senha'),
    path('AlterarSenha/',AlterarSenha,name = 'Alterar_Senha'),
    path('Logout/',Logout,name = 'Logout')
]