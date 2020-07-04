from django.contrib import admin
from .models import *
from import_export import admin as ad

@admin.register(produtos)
class ProdutosAdmin(ad.ImportExportModelAdmin):
    list_display = ['name','Status']
    search_fields = ['name','Status']
@admin.register(pedidos)
class PedidosAdmin(ad.ImportExportModelAdmin):
    list_display = ['usuario','status','pagamento','criado']
    search_fields = ['usuario__Nome_completo','status','pagamento']

@admin.register(itemPedido)
class ItemPedidosAdmin(ad.ImportExportModelAdmin):
    list_display = ['pedido','produto']
    search_fields = ['pedido__pk']