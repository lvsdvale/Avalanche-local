from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic import ListView,View

# Create your views here.
class Engenhariadas(ListView):
    template_name = 'Engenhariadas.html'
    model = engenhariadas
    paginate_by = 10
    ordering = '-pub_date'

def EngenhariadasView(request, slug):
    Engenhariadas = get_object_or_404(engenhariadas, slug = slug)
    if request.method == 'POST':
        inscricao = parceladao.objects.filter(email=request.user.email, engenhariadas=Engenhariadas)
        if inscricao.exists() is False:
            inscricao.objects.inscrever(usuario=request.user, engenhariadas=Engenhariadas)
            messages.success(request, "Inscrito no parceladão com sucesso")
        else:
            messages.info(request,"Você já está inscrito no parceladão desse ano")
    context = {
        "Engenhariadas": Engenhariadas,
    }
    return render(request, 'PadraoEngenhariadas.html', context)