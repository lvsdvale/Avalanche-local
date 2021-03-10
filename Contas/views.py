from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from Avalancheutfpr.models import inscricao_modalidades, inscricao_campanhas_sociais, inscricao_E_sports, eventos, campanhas
from Avalancheutfpr.services import Send_Sign_Mail, Send_Reset_Mail
from random import choice
from datetime import datetime
# views de login

def Cadastrar_usuarios(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            Nome = form.cleaned_data.get('first_name ')
            email = form.cleaned_data.get('email')
            messages.success(request, "Cadastro Realizado com Sucesso")
            User = authenticate(username=email, password=raw_password)
            Send_Sign_Mail(Email=email,Nome=Nome)
            login(request, User)
            return redirect('Home')
    else:
        form = Cadastro()
    context = {
        "form": form
    }
    return render(request, 'Cadastro_Usuarios.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com Sucesso')

            else:
                messages.error(request, "as credenciais estão incorretas")

        form_login = AuthenticationForm()
        context = {'form': form_login}
        return render(request, 'Login.html', context)


@login_required(redirect_field_name='Login')
def AlterarSenha(request):
    if request.method == 'POST':
        oldpassword = request.POST["old_password"]
        password1 = request.POST["new_password1"]
        password2 = request.POST["new_password2"]
        if request.user.check_password(oldpassword) and password1 == password2:
            if oldpassword == password1:
                messages.error(request,"A senha antiga é igual a nova")
            else:
                request.user.set_senha(password1)
                messages.success(request, 'Senha alterada com sucesso')
                user = authenticate(username=request.user, password=password1)
                login(request,user)
                return redirect("Minha_Conta")
        else:
            if request.user.check_password(oldpassword) is False:
                messages.error(request, 'A senha antiga está incorreta')
            if password1 != password2:
                messages.error(request, 'A confirmação de senha falhou')
    form = PasswordChangeForm(user=request.user)
    context = {'form':form }
    return render(request, 'AlterarSenha.html', context)


@login_required(redirect_field_name='Home')
def Logout(request):
    logout(request)
    messages.success(request,"Logout realizado com Sucesso")
    return redirect('Home')

@login_required
def Minha_Conta(request):
    if request.user.is_authenticated:
        hoje = datetime.now()
        Eventos = eventos.objects.filter(data__gt=hoje)
        Campanhas = campanhas.objects.filter(data__gt=hoje)
        context = {}
        context['Eventos'] = Eventos
        context['Campanhas'] = Campanhas
        return render(request,'Minha_Conta.html',context)
    return redirect('Login')

@login_required
def Meus_Dados(request):
    if request.user.is_authenticated:
        Inscricao_modalidades = inscricao_modalidades.objects.filter(usuario = request.user).order_by('modalidade')
        Inscricao_campanhas_sociais = inscricao_campanhas_sociais.objects.filter(usuario = request.user).order_by('campanha')
        Inscricao_E_sports = inscricao_E_sports.objects.filter(usuario = request.user).order_by('game')
        context = {}
        context['Inscricao_esportes'] = Inscricao_modalidades
        context['Inscricao_campanhas'] = Inscricao_campanhas_sociais
        context['Inscricao_E_sports'] = Inscricao_E_sports
        return render(request,'Meus_Dados.html',context)
    return redirect('Login')


def Resetar(request):
    if request.method == 'POST':
        form = Reset(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get("Email")
                cpf = form.cleaned_data.get("CPF")
                Usuario = user.objects.get(CPF = cpf,email= email)

                caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                Nova_senha = ''
                for i in range(8):
                    Nova_senha += choice(caracteres)
                Usuario.set_senha(Nova_senha)
                Send_Reset_Mail(email,Nova_senha)
                messages.success(request,"Sua nova senha foi enviada para seu email")
            except:
                messages.error(request, "Usuário não cadastrado no banco de dados")
    else:
        form = Reset()
    context = {
        'form':form
    }
    return render(request, 'ResetarSenha.html', context)
