from django.urls import path
from .views import *
urlpatterns = [
    path('Cadastro/', Cadastrar_usuarios,name = 'Cadastro'),
    path('Login/',Login,name = 'Login'),
    path('Minha-Conta/',Minha_Conta,name = 'Minha_Conta'),
    path('ResetarSenha/',Resetar,name = 'Resetar_Senha'),
    path('Logout/',Logout,name = 'Logout')
]