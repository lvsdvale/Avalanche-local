from django.contrib import admin
from .models import *
from import_export import admin as ad

@admin.register(produtos)
class ProdutosAdmin(ad.ImportExportModelAdmin):
    list_display = ['name','Status']
@admin.register(pedidos)
class PedidosAdmin(ad.ImportExportModelAdmin):
    list_display = ['usuario','status','pagamento','criado']
@admin.register(itemPedido)
class ItemPedidosAdmin(ad.ImportExportModelAdmin):
    list_display = ['pedido','produto']