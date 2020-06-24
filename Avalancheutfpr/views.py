from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from django.views.generic import View,TemplateView,ListView
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

# Views das paginas referentes a atletica.
class Home(TemplateView):
    template_name = 'index.html'
def Contatos(request):
    initial = None
    if request.user.is_authenticated:
        initial = {
            'name':request.user.get_nome_completo(),
            'email':request.user.get_email()
                   }
    if request.method == 'POST':
        form = Form_contatos(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            messages.success(request, "Recebemos seu contato e logo retornaremos")
            form = Form_contatos(initial=initial)
            context = {
                'form': form
            }
            return render(request, 'Contatos.html', context)

        else:
            messages.error(request, 'Houve falha no seu contato, verifique os campos do formulario')
    else:
        form = Form_contatos(initial=initial)
    context = {
        'form':form
    }
    return render(request,'Contatos.html',context)

class SobreNos(TemplateView):
    template_name = 'SobreNos.html'

# Views Referentes a página de Eventos
class Eventos(ListView):
    template_name = 'Eventos.html'
    model = eventos
    paginate_by = 5
    ordering = '-pub_date'


def Eventos_view(request, slug):
    eve = get_object_or_404(eventos, slug = slug)
    context = {
        "Eventos": eve
    }
    return render(request, 'PadraoEventos.html', context)

def Eventos_midias(request,slug):
    eve = get_object_or_404(eventos,slug=slug)
    Midias = media.objects.filter(tag=eve.name).order_by('-pub_date')
    context = {
        'Eventos':eve,
        'Midias':Midias
    }
    return render(request,'MidiasEventos.html',context)


# Views Referentes a página de Esportes
class Esportes(TemplateView):
    template_name = 'Esportes.html'
    def get_context_data(self, **kwargs):
        context = super(Esportes,self).get_context_data(**kwargs)
        context['Modalidades'] = modalidades.objects.all().order_by('name')
        return context
@csrf_exempt
def Modalidades_view(request, slug):
    Modalidades = get_object_or_404(modalidades, slug=slug)
    initial = None
    if request.user.is_authenticated:
        initial = {'usuario':request.user,
                   'modalidade':Modalidades,
                   }
    if request.method == 'POST':
        form = Form_incricao_esportes(request.POST,initial=initial)
        if form.is_valid():
            inscricao = inscricao_modalidades.objects.filter(usuario = request.user,modalidade = Modalidades)
            if inscricao.exists() is False:
                form.save()
                messages.success(request,"Inscrito na modalidade com sucesso")
            else:
                messages.info(request,"Você já está inscrito nessa Modalidade")
            form.cleaned_data
        else:
            messages.error(request, 'inscrição falhou')
    else:
        form = Form_incricao_esportes(initial=initial)

    context = {
        "Modalidades": Modalidades,'form':form,
    }
    return render(request, 'PadraoModalidades.html', context)

def Modalidades_midias(request,slug):
    Modalidades = get_object_or_404(modalidades,slug= slug)
    Midias = media.objects.filter(tag=Modalidades.name).order_by('-pub_date')
    context = {
        'Modalidades':Modalidades,
        'Midias':Midias
    }
    return render(request,'MidiasModalidades.html',context)


# Views Referentes a página de Social

class Social(ListView):
    template_name = 'Social.html'
    model = campanhas
    paginate_by = 5
    ordering = '-pub_date'

def Campanhas_view(request, slug):
    Campanhas = get_object_or_404(campanhas, slug=slug)
    initial = None
    if request.user.is_authenticated:
        initial = {'usuario':request.user,
                   'campanha':Campanhas,
                   }
    if request.method == 'POST':
        form = Form_inscricao_campanhas(request.POST, initial=initial)
        if form.is_valid():
            inscricao = inscricao_campanhas_sociais.objects.filter(usuario=request.user,campanha = Campanhas)
            if inscricao.exists() is False:
                form.save()
                messages.success(request, "Inscrito na ação com sucesso")
            else:
                messages.info(request,"Você já está inscrito nessa Campanha")
            form.cleaned_data
        else:
            messages.error(request, 'inscrição falhou')
    else:
        form = Form_inscricao_campanhas(initial=initial)


    context = {
        "Campanhas": Campanhas,'form':form
    }
    return render(request, 'CampanhasPadrao.html', context)

def Campanhas_midias(request,slug):
    Campanhas = get_object_or_404(campanhas,slug = slug)
    Midias = media.objects.filter(tag = Campanhas.name).order_by('-pub_date')
    context = {
        'Campanhas':Campanhas,
        'Midias':Midias
    }
    return render(request,'MidiasCampanhas.html',context)
# Views Referentes a página de plano Sócio
class Socio(TemplateView):
    template_name = 'Socio.html'

# Views Referentes a página de E-sports
class E_sports(TemplateView):
    template_name = 'E-sports.html'
    def get_context_data(self, **kwargs):
        context = super(E_sports, self).get_context_data(**kwargs)
        context['Games'] = games.objects.all().order_by('-pub_date')
        return context


def Games_view(request, slug):
    Games = get_object_or_404(games, slug = slug)
    initial = None
    if request.user.is_authenticated:
        initial = {'usuario':request.user,
                   'game':Games
                   }
    if request.method == 'POST':
        form = Form_inscricao_games(request.POST, initial=initial)
        if form.is_valid():
            inscricao = inscricao_E_sports.objects.filter(usuario=request.user, game=Games)
            if inscricao.exists() is False:
                form.save()
                messages.success(request, "Inscrito na modalidade de E-sports com sucesso")
            else:
                messages.info(request,"Você já está inscrito nesse game")
            form.cleaned_data
        else:
            messages.error(request, 'inscrição falhou')
    else:
        form = Form_inscricao_games(initial=initial)

    context = {
        "Games": Games,
        "form":form
    }
    return render(request, 'PadraoGames.html', context)

#Diretoria
def Diretoria(request):
    Diretoria= diretoria.objects.all().order_by('-area')
    initial = None
    if request.user.is_authenticated:
        initial = {'usuario':request.user
                   }
    if request.method == 'POST':
        form = Form_inscricao_processo_seletivo(request.POST, initial=initial)
        if form.is_valid():
            inscricao = inscricao_processo_seletivo.objects.filter(usuario = request.user)
            if inscricao is None:
                form.save()
                messages.success(request, "Parabéns, você demonstrou interesse em fazer parte do time, logo entraremos em contato")
            else:
                messages.info(request,"Você já está inscrito no processo seletivo Avalanche, logo entraremos em contato")
            form.cleaned_data
        else:
            messages.error(request, 'inscrição falhou')
    else:
        form = Form_inscricao_processo_seletivo(initial=initial)

    context = {
        "Diretoria": Diretoria,
        "form":form
    }
    return render(request, 'Diretoria.html', context)

#Galeria
class Galeria(TemplateView):
    template_name = 'Galeria.html'
    def get_context_data(self, **kwargs):
        context = super(Galeria,self).get_context_data(**kwargs)
        context['Midias'] = media.objects.all().order_by('tag')
        return context
#Erros
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
