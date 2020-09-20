from django.contrib import admin
from .models import *

@admin.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['name','categoria','pub_date']
    search_fields = ['name','categoria']

@admin.register(custo)
class CustoAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(contaspagar)
class PagarAdmin(admin.ModelAdmin):
    list_display = ['name','Custo','pub_date']
    search_fields = ['name','Custo','fornecedor']

@admin.register(contasreceber)
class ReceberAdmin(admin.ModelAdmin):
    list_display = ['name','Custo','pub_date']
    search_fields = ['name','Custo']