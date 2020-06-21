from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from django.views.generic import View,TemplateView,FormView,ListView
from django.core.paginator import Paginator
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
    Midias_list = media.objects.all().order_by('name')
    Midias = []
    for midia in Midias_list:
        if midia.tag == eve.name:
            Midias.append(midia)
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
            if inscricao is None:
                form.save()
                messages.success(request,"inscrito na modalidade com sucesso")
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
    Midias_list = media.objects.all().order_by('name')
    Midias = []
    for midia in Midias_list:
        if midia.tag == Modalidades.name:
            Midias.append(midia)
    context = {
        'Modalidades':Modalidades,
        'Midias':Midias
    }
    return render(request,'MidiasModalidades.html',context)


# Views Referentes a página de Social

def Social(request):
    campanhas_list = campanhas.objects.all().order_by('-pub_date')
    paginator = Paginator(campanhas_list, 5)
    page = request.GET.get('page')
    Campanhas = paginator.get_page(page)
    context = {"Campanhas": Campanhas
               }
    return render(request, 'Social.html', context)


def Campanhas_view(request, slug):
    Campanhas = get_object_or_404(campanhas, slug=slug)
    initial = None
    if request.user.is_authenticated:
        tag = f'{Campanhas.id}.{request.user.get_CPF()}'
        initial = {'name': request.user.get_nome_completo(),
                   'email':request.user.get_email(),
                   'CPF':request.user.get_CPF(),
                   'Curso': request.user.get_Curso(),
                   'Ra': request.user.get_Registro_Academico(),
                   'Campanha': Campanhas.name,
                   'local':Campanhas.local,
                   'Telefone': request.user.get_Telefone(),
                   'tag': tag
                   }
    if request.method == 'POST':
        form = Form_inscricao_campanhas(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            messages.success(request, "inscrito na ação com sucesso")
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
    Midias_list = media.objects.all().order_by('name')
    Midias = []
    for midia in Midias_list:
        if midia.tag == Campanhas.name:
            Midias.append(midia)
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
        tag = f'{Games.id}.{request.user.get_CPF()}'
        initial = {'name': request.user.get_nome_completo(),
                   'Curso': request.user.get_Curso(),
                   'Ra': request.user.get_Registro_Academico(),
                   'Game': Games.name,
                   'Telefone': request.user.get_Telefone(),
                   'tag': tag
                   }
    if request.method == 'POST':
        form = Form_inscricao_games(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            messages.success(request, "inscrito na modalidade de E-sports com sucesso")
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
        initial = {'name': request.user.get_nome_completo(),
                   'email':request.user.get_email(),
                   'Curso': request.user.get_Curso(),
                   'Ra': request.user.get_Registro_Academico(),
                   'Telefone': request.user.get_Telefone(),
                   }
    if request.method == 'POST':
        form = Form_inscricao_processo_seletivo(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            messages.success(request, "Parabéns, você demonstrou interesse em fazer parte do time, logo entraremos em contato")
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
