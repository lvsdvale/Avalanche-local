from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.views.generic import TemplateView,ListView
from django.contrib import messages
from django.db import models
from .services import *
from oscar.core.loading import get_model
Country = get_model('address', 'Country')
# Views das paginas referentes a atletica.
class Home(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(Home,self).get_context_data(**kwargs)
        context["Modalidades"] = modalidades.objects.all().order_by("?")
        return context

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
    def get_context_data(self, **kwargs):
        context = super(SobreNos, self).get_context_data(**kwargs)
        context["Diretoria"] = diretoria.objects.all().order_by('cargo')
        return context


# Views Referentes a página de Eventos
class Eventos(ListView):
    template_name = 'Eventos.html'
    context_object_name = 'eventos'
    paginate_by = 5
    ordering = '-data'
    def get_queryset(self):
        queryset = eventos.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(name__icontains=q) | models.Q(descricao__icontains=q)
            )

        return queryset


def Eventos_view(request, slug):
    eve = get_object_or_404(eventos, slug = slug)
    Midias = media.objects.filter(tag=eve.name).order_by('-pub_date')
    context = {
        "Eventos": eve,
        "Midias":Midias,
    }
    return render(request, 'PadraoEventos.html', context)


# Views Referentes a página de Esportes
class Esportes(TemplateView):
    template_name = 'Esportes.html'
    def get_context_data(self, **kwargs):
        context = super(Esportes,self).get_context_data(**kwargs)
        context['Modalidades'] = modalidades.objects.all().order_by('name')
        return context


    def get_queryset(self):
        queryset = modalidades.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(name__icontains=q) | models.Q(descricao__icontains=q)
            )
        return queryset

def Modalidades_view(request, slug):
    Modalidades = get_object_or_404(modalidades, slug=slug)
    if request.method == 'POST':
        inscricao = inscricao_modalidades.objects.filter(email = request.user.email,modalidade = Modalidades)
        if inscricao.exists() is False:
            inscricao_modalidades.objects.inscrever(usuario=request.user,modalidade= Modalidades)
            Send_Esportes_Mail(request.user,Modalidades)
            messages.success(request,"Inscrito na modalidade com sucesso")
        else:
            messages.info(request,"Você já está inscrito nessa Modalidade")
    Midias = media.objects.filter(tag=Modalidades.name).order_by('-pub_date')
    context = {
        "Modalidades": Modalidades,
        "Midias":Midias
    }
    return render(request, 'PadraoModalidades.html', context)

# Views Referentes a página de Social

class Social(ListView):
    template_name = 'Social.html'
    context_object_name = 'campanhas'
    ordering = '-pub_date'


    def get_queryset(self):
        queryset = campanhas.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(name__icontains=q) | models.Q(descricao__icontains=q) | models.Q(local__icontains=q)
            )

        return queryset

def Campanhas_view(request, slug):
    Campanhas = get_object_or_404(campanhas, slug=slug)
    if request.method == 'POST':
        inscricao = inscricao_campanhas_sociais.objects.filter(email = request.user.email,campanha = Campanhas)
        if inscricao.exists() is False:
            inscricao_campanhas_sociais.objects.inscrever(usuario = request.user,Campanha = Campanhas
            )
            Send_Acao_Mail(usuario=request.user,campanha=Campanhas)
            messages.success(request, "Inscrito na ação com sucesso")
        else:
            messages.info(request,"Você já está inscrito nessa Campanha")
    Midias = media.objects.filter(tag=Campanhas.name).order_by('-pub_date')
    context = {
        "Campanhas": Campanhas,
        "Midias":Midias,
    }
    return render(request, 'CampanhasPadrao.html', context)

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
    if request.method == 'POST':
        inscricao = inscricao_E_sports.objects.filter(email=request.user.email, game=Games)
        if inscricao.exists() is False:
            inscricao_E_sports.objects.inscrever(usuario=request.user, game=Games)
            Send_E_sports_Mail(usuario=request.user,game=Games)
            messages.success(request, "Inscrito na modalidade de E-sports com sucesso")
        else:
            messages.info(request,"Você já está inscrito nessa Modalidade")
    Midias = media.objects.filter(tag=Games.name).order_by('-pub_date')
    context = {
        "Games": Games,
        "Midias":Midias
    }
    return render(request, 'PadraoGames.html', context)

#Diretoria
def Diretoria(request):
    Diretoria= diretoria.objects.all().order_by('cargo')
    context = {
        "Diretoria": Diretoria,

    }
    return render(request, 'Diretoria.html', context)

#Galeria
class Galeria(TemplateView):
    template_name = 'Galeria.html'
    def get_context_data(self, **kwargs):
        context = super(Galeria,self).get_context_data(**kwargs)
        context['Albuns'] = album.objects.all().order_by('-data')
        return context

def GaleriaView(request, slug):
    albuns = get_object_or_404(album, slug=slug)
    pics = fotos.objects.filter(album=albuns)
    context = {
        'album':albuns,
        'fotos':pics
    }
    return render(request,'PadraoAlbuns.html',context=context)
#Competiçoes e Jogos
class Competicoes(ListView):
    template_name = 'Competicoes.html'
    context_object_name = 'competicoes'
    ordering = '-pub_date'
    def paginate(self):
        if not self.resquest.is_mobile:
            paginate_by = 5
    def get_queryset(self):
        queryset = competicoes.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(name__icontains=q) | models.Q(descricao__icontains=q) | models.Q(local__icontains=q)
            )

        return queryset
class Bateria(TemplateView):
    template_name = 'Bateria.html'
    def get_context_data(self, **kwargs):
        context = super(Bateria,self).get_context_data(**kwargs)
        context['Diretoria'] = bateria.objects.all().order_by('cargo')
        return context

class Cheers(TemplateView):
    template_name = 'Cheers.html'
    def get_context_data(self, **kwargs):
        context = super(Cheers,self).get_context_data(**kwargs)
        context['Diretoria'] = cheers.objects.all().order_by('cargo')
        return context


class EsportsHistoria(TemplateView):
    template_name = 'EsportsHistoria.html'
    def get_context_data(self, **kwargs):
        context = super(EsportsHistoria,self).get_context_data(**kwargs)
        context['Diretoria'] = esports.objects.all().order_by('cargo')
        return context

class BBBA(TemplateView):
    template_name = 'BBBA.html'
#Erros
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
