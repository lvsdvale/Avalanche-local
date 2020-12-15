from django.contrib import admin
from .models import *
from import_export import admin as ad

@admin.register(catalogo)
class CatalogoAdmin(ad.ImportExportModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

@admin.register(produtobase)
class ModelosAdmin(ad.ImportExportModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

@admin.register(produtos)
class ProdutosAdmin(ad.ImportExportModelAdmin):
    search_fields = ['name','Status']

@admin.register(itemcarrinho)
class CarrinhoAdmin(ad.ImportExportModelAdmin):
    list_display = ['chave',]
@admin.register(pedidos)
class PedidosAdmin(ad.ImportExportModelAdmin):
    list_display = ['usuario','status','pagamento','criado']
    search_fields = ['usuario__Nome_completo','status','pagamento']

@admin.register(itemPedido)
class ItemPedidosAdmin(ad.ImportExportModelAdmin):
    list_display = ['pedido','produto']
    search_fields = ['pedido__pk']