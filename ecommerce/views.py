from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic import RedirectView,TemplateView,ListView
from .forms import itemcarrinhoformset
from django.contrib import messages
from django.urls import reverse
from .signals import *
from .models import *
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from pagseguro import PagSeguro
from picpay import PicPay

# Create your views here.
class Lojinha(ListView):
    template_name = 'Produtos.html'
    context_object_name = 'produtobase'
    paginate_by = 10
    ordering = 'pub_date'

    def get_queryset(self):
        queryset = produtobase.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(name__icontains=q) | models.Q(descricao__icontains=q)
            )

        return queryset

def Produtobase_view(request,slug):
    Produtobase = get_object_or_404(produtobase,slug=slug)
    if request.method == 'POST':
        answer = request.POST['Modelo']
        if answer == '0':
            messages.info(request,'Quase lá, insira o modelo que deseja comprar')
        else:
            return redirect('Adicionar_produto',pk = answer)
    context = {
        'produtobase':Produtobase
    }
    return render(request,'PadraoProdutosBase.html',context)

def criar_item_view(request,pk):
    produto = get_object_or_404(produtos, pk=pk)
    if request.session.session_key is None:
        request.session.save()
    if request.user.is_anonymous:
        item, criado = itemcarrinho.objects.adicionar(request.session.session_key, produto)
    else:
        if not request.user.get_socio:
            item, criado = itemcarrinho.objects.adicionar(request.session.session_key, produto)
        else:
            item, criado = itemcarrinho.objects.adicionar_socio(request.session.session_key, produto)
    if criado:
        messages.success(request, 'Produto adicionado ao carrinho')
    else:
        messages.success(request, 'Quantidade produto atualizado carrinho')

    return redirect('Carrinho')


class Carrinho(TemplateView):
    template_name = 'Carrinho.html'

    def get_formset(self,clear = False):
        if self.request.session.session_key:
            if clear:
                formset = itemcarrinhoformset(
                queryset = itemcarrinho.objects.filter(chave = self.request.session.session_key)
                )
            else:
                formset = itemcarrinhoformset(
                    queryset=itemcarrinho.objects.filter(chave=self.request.session.session_key),
                    data=self.request.POST or None
                )
        else:
            formset = itemcarrinhoformset(
                queryset=itemcarrinho.objects.none()
            )

        return formset

    def get_context_data(self, **kwargs):
        context = super(Carrinho,self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self,request,*args,**kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request,'Carrinho Atualizado com Sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)

class Checkout(LoginRequiredMixin,TemplateView):
    template_name = 'Checkout.html'
    login_url = 'Login'
    def get(self,request,*args,**kwargs):
        chave = request.session.session_key
        if chave and itemcarrinho.objects.filter(chave = chave).exists():
            itens = itemcarrinho.objects.filter(chave = chave)
            pedido = pedidos.objects.adicionar(usuario = request.user,itenscarrinho=itens)
            for item in itens:
                Produtos = produtos.objects.filter(name = item.produto)
                for Produto in Produtos:
                    Produtos.update(estoque = Produto.estoque-item.quantidade)
            itens.delete()

        else:
            messages.info(request,'O Carrinho está Vazío')
            return redirect('Carrinho')
        response = super(Checkout,self).get(request,*args,**kwargs)
        response.context_data['Pedido'] = pedido
        return response

class MeusPedidosView(LoginRequiredMixin,ListView):
    template_name = 'MeusPedidos.html'
    login_url = 'Login'
    def get_queryset(self):
        return pedidos.objects.filter(usuario  = self.request.user)

class PedidoView(LoginRequiredMixin,DetailView):
    template_name = 'PadraoPedido.html'
    query_pk_and_slug = 'pk'
    login_url = 'Login'
    def get_queryset(self):
        return pedidos.objects.filter(usuario = self.request.user)

class PagseguroView(LoginRequiredMixin,RedirectView):
    login_url = 'Login'
    def get_redirect_url(self, *args, **kwargs):
        pedidos_pk = self.kwargs.get('pk')
        pedido = get_object_or_404(pedidos.objects.filter(usuario = self.request.user),pk = pedidos_pk)
        pg = pedido.pagseguro()
        self.request.build_absolute_uri(
            reverse('Meus_Pedidos')
        )
        response = pg.checkout()
        return response.payment_url
@csrf_exempt
def PagseguroNotification(request):
    notification_code = request.POST.get('notificationCode', None)
    if notification_code:
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        notification_data = pg.check_notification(notification_code)
        status = notification_data.status
        reference = notification_data.reference
        try:
            pedido = pedidos.objects.get(pk=reference)
        except pedidos.DoesNotExist:
            pass
        else:
            pedido.pagseguro_update_status(status)
    return HttpResponse('OK')
class PicpayView(LoginRequiredMixin,RedirectView):
    login_url = 'Login'
    def get_redirect_url(self, *args, **kwargs):
        pedidos_pk = self.kwargs.get('pk')
        pedido = get_object_or_404(pedidos.objects.filter(usuario = self.request.user),pk = pedidos_pk)
        pc = pedido.picpay()
        payment = pc.payment(
            reference_id=pedidos_pk,
            callback_url=f'http://localhost:8000/Notificacoes/picpay/{pedidos_pk}',
            return_url=self.request.build_absolute_uri(
            reverse('Meus_Pedidos')
            ),
            value=pedido.total(),
            buyer={
                "firstName": self.request.user.Nome_completo,
                "lastName": self.request.user.Nome_completo,
                "document": self.request.user.CPF,
                "email": self.request.user.email,
                "phone": self.request.user.Telefone,
            },
        )
        return payment['paymentUrl']
@csrf_exempt
def PicpayNotification(request,pk):
    pc = PicPay(
        x_picpay_token=settings.X_PICPAY_TOKEN, x_seller_token=settings.X_SELLER_TOKEN
    )
    pedido= pedidos.objects.get(pk=pk)
    status = pc.status(reference_id=pk)
    pedido.picpay_update_status(status['status'])
    return HttpResponse(200)