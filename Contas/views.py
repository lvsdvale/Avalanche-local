from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm,PasswordChangeForm
from django.views.decorators.csrf import  csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from Avalancheutfpr.models import inscricao_modalidades,inscricao_campanhas_sociais,inscricao_E_sports,eventos,campanhas
from Avalancheutfpr.services import Send_Sign_Mail,Send_Reset_Mail
from random import choice
# views de login
@csrf_exempt
def Cadastrar_usuarios(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            Nome = form.cleaned_data.get('Nome_completo')
            email = form.cleaned_data.get('email')
            messages.success(request,"Cadastro Realizado com Sucesso")
            User = authenticate(username=username, password=raw_password)
            Send_Sign_Mail(Email=email,Nome=Nome)
            return redirect('Home')
    else:
        form = Cadastro()
    context = {
        "form": form
    }
    return render(request, 'Cadastro_Usuarios.html', context)

@csrf_exempt
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
                messages.success(request,'Login realizado com Sucesso')
                return redirect('Home')
            else:
                messages.error(request, "as credenciais estão incorretas")

        form_login = AuthenticationForm()
        context = {'form': form_login
               }

        return render(request, 'Login.html', context)

@login_required(redirect_field_name='Login')
@csrf_exempt
def AlterarSenha(request):
    if request.method == 'POST':
        oldpassword = request.POST["old_password"]
        password1 = request.POST["new_password1"]
        password2 = request.POST["new_password2"]
        if request.user.check_password(oldpassword) and password1==password2:
            if oldpassword==password1:
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
        Eventos = eventos.objects.all().order_by('-pub_date')
        Campanhas = campanhas.objects.all().order_by('-pub_date')
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
            email = form.cleaned_data.get("Email")
            cpf = form.cleaned_data.get("CPF")
            Usuario = user.objects.get(CPF = cpf,email= email)
            if Usuario == None:
                messages.error(request,"Dados inválidos")
            else:
                caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                Nova_senha = ''
                for i in range(8):
                    Nova_senha += choice(caracteres)
                Usuario.set_senha(Nova_senha)
                Send_Reset_Mail(email,Nova_senha)
                messages.success(request,"Sua nova senha foi enviada para seu email")
    else:
        form = Reset()
    context = {
        'form':form
    }
    return render(request, 'ResetarSenha.html', context)
