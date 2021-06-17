from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.views.generic import TemplateView,ListView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from Avalancheutfpr.models import *
from Engenhariadas.models import *
from Blog.models import *
from Contas.models import *
from datetime import datetime
def Dashboard(request):
    if request.user.is_authenticated == False and request.user.is_superuser==False:
        return redirect('Home')
    else:
        hoje = datetime.now()
        Pedidos = pedidos.objects.all()
        Usuarios = user.objects.all()
        Socios = user.objects.filter(Socio = True)
        Atletas = inscricao_modalidades.objects.all()
        Acoes = inscricao_campanhas_sociais.objects.all()
        E_sports = inscricao_E_sports.objects.all()
        Eventos = eventos.objects.filter(data__gt =  hoje)
        Campanhas = campanhas.objects.filter(data__gt =  hoje)
        context = {}
        context['Eventos'] = Eventos
        context['Campanhas'] = Campanhas
        context["Pedidos"] = Pedidos
        context["Usuarios"] = Usuarios
        context["Atletas"] = Atletas
        context["Acoes"] = Acoes
        context["E_sports"] = E_sports
        context["Socios"] = Socios
        return render(request, 'Dashboard.html', context)