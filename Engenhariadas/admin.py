from django.contrib import admin
from import_export import admin as ad
from .models import *

# Register your models here.
@admin.register(engenhariadas)
class EngenhariadasAdmin(admin.ModelAdmin):
    list_display = ['name','Status','data']
    search_fields = ['name','Status','data']

@admin.register(parceladao)
class ParceladaoAdmin(ad.ImportExportModelAdmin):
    list_display = ['name','email','data']
    search_fields = ['name','email','telefone','data']

@admin.register(pagamentos)
class PagamentosAdmin(ad.ImportExportModelAdmin):
    list_display = ['name','email','data']
    search_fields = ['name','email','cpf ','telefone','deposito','engenhariadas','pagamento','data']