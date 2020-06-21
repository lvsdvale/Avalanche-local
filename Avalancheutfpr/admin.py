from django.contrib import admin
from .models import *
from import_export import admin as ad
@admin.register(eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ['name','Status','data']
@admin.register(modalidades)
class ModalidadesAdmin(admin.ModelAdmin):
    list_display = ['name','Status']
@admin.register(games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['name','Status']
@admin.register(campanhas)
class CampanhasAdmin(admin.ModelAdmin):
    list_display = ['name','Status','data']

@admin.register(inscricao_modalidades)
class Incricao_Esportes_Admin(ad.ImportExportModelAdmin):
    list_display = ['usuario','data']

@admin.register(inscricao_Campanhas)
class Incricao_Campanhas_Admin(ad.ImportExportModelAdmin):
    list_display = ['name','Ra']

@admin.register(inscricao_games)
class Incricao_Games_Admin(ad.ImportExportModelAdmin):
    list_display = ['name','Ra']
@admin.register(processo_seletivo)
class Incricao_Processo_Seletivo(ad.ImportExportModelAdmin):
    list_display = ['name','Ra']
@admin.register(contatos)
class ContatosAdmin(admin.ModelAdmin):
    list_display = ['email','assunto']
@admin.register(diretoria)
class Diretoria(admin.ModelAdmin):
    list_display = ['name','area']

@admin.register(media)
class media(admin.ModelAdmin):
    list_display = ['name','tag']