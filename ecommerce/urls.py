from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
        path('Produtos/', Lojinha.as_view(), name='Produtos'),
        path('Produtos/<slug:slug>',Produtobase_view.as_view(),name = 'ProdutosBase_view'),
        path('Produtos/Modelos/<slug:slug>',Produto_view.as_view(),name = 'Produtos_view'),
        path('Carrinho/adicionar/<slug:slug>',criar_item_view.as_view(),name = 'Adicionar_produto'),
        path('Carrinho/',Carrinho.as_view(),name = 'Carrinho'),
        path('Checkout/',Checkout.as_view(),name = 'Checkout'),
        path('Meus_Pedidos/',MeusPedidosView.as_view(),name = 'Meus_Pedidos'),
        path('Meus_Pedidos/<int:pk>',PedidoView.as_view(),name = 'PedidoView'),
        path('Checkout/<int:pk>/pagseguro',PagseguroView.as_view(),name = 'PagSeguro'),
        path('Notificacoes/pagseguro',PagseguroNotification,name = 'pagseguro_notification'),
        path('Checkout/<int:pk>/picpay',PicpayView.as_view(),name = 'Picpay'),
        path('Notificacoes/picpay/<int:pk>',PicpayNotification,name = 'Picpay_notification'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)