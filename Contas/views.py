from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from Avalancheutfpr.models import inscricao_modalidades,inscricao_campanhas_sociais,inscricao_E_sports,eventos,campanhas


# views de login
@csrf_exempt
def Cadastrar_usuarios(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request,"Cadastro Realizado com Sucesso")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Cadastro')
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



@login_required(redirect_field_name='Home')
def Logout(request):
    logout(request)
    messages.success(request,"Logout realizado com Sucesso")
    return redirect('Home')

def Minha_Conta(request):
    if request.user.is_authenticated:
        Inscricao_modalidades = inscricao_modalidades.objects.filter(usuario = request.user).order_by('modalidade')
        Inscricao_campanhas_sociais = inscricao_campanhas_sociais.objects.filter(usuario = request.user).order_by('campanha')
        Inscricao_E_sports = inscricao_E_sports.objects.filter(usuario = request.user).order_by('game')
        Eventos = eventos.objects.all().order_by('-pub_date')
        Campanhas = campanhas.objects.all().order_by('-pub_date')
        context = {}
        context['Eventos'] = Eventos
        context['Campanhas'] = Campanhas
        context['Inscricao_esportes'] = Inscricao_modalidades
        context['Inscricao_campanhas'] = Inscricao_campanhas_sociais
        context['Inscricao_E_sports'] = Inscricao_E_sports
        return render(request,'Minha_Conta.html',context)
    return redirect('Login')
