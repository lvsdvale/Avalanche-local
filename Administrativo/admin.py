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
