from django.contrib import admin
from import_export import admin as ad
from .models import *
@admin.register(user)
class useradmin(ad.ImportExportModelAdmin):
    list_display = ('Nome_completo','email','CPF')
    search_fields = ('Nome_completo','email','CPF','Curso','Registro_Academico','Telefone')



