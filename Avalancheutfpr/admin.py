from django.contrib import admin
from .models import *
from import_export import admin as ad
from django_summernote.admin import SummernoteModelAdmin

@admin.register(eventos)
class EventosAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao',)
    list_display = ['name', 'Status', 'data']
    search_fields = ['name', 'Status', 'data']


@admin.register(modalidades)
class ModalidadesAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao',)
    list_display = ['name', 'Status']


@admin.register(games)
class GamesAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao',)
    list_display = ['name', 'Status']


@admin.register(campanhas)
class CampanhasAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao',)
    list_display = ['name', 'Status', 'data']
    search_fields = ['name', 'local', 'data']


@admin.register(inscricao_modalidades)
class Incricao_Esportes_Admin(ad.ImportExportModelAdmin):
    list_display = ['name', 'get_modalidade', 'data']
    search_fields = ['name', 'email', 'curso', 'Ra', 'modalidade', 'data']
    def get_modalidade(self, obj):
        return obj.modalidade

    get_modalidade.short_description = 'Modalidade'
    get_modalidade.admin_order_field = 'Modalidade'


@admin.register(inscricao_campanhas_sociais)
class Incricao_Campanhas_Admin(ad.ImportExportModelAdmin):
    list_display = ['name', 'get_campanha', 'data']
    search_fields = ['name', 'email', 'curso', 'Ra', 'campanha', 'data']
    def get_campanha(self, obj):
        return obj.campanha
    get_campanha.short_description = 'Campanha'
    get_campanha.admin_order_field = 'Campanha'


@admin.register(inscricao_E_sports)
class Incricao_Games_Admin(ad.ImportExportModelAdmin):
    list_display = ['name', 'get_game','data']
    search_fields = ['name', 'email', 'curso', 'Ra', 'game', 'data']
    def get_game(self, obj):
        return obj.game
    get_game.short_discription = 'Modalidade Esports'
    get_game.admin_order_field = 'Modalidade Esports'
@admin.register(contatos)
class ContatosAdmin(admin.ModelAdmin):
    list_display = ['email', 'assunto']
    search_fields = ['name', 'email', 'assunto']


@admin.register(diretoria)
class Diretoria(admin.ModelAdmin):
    list_display = ['name', 'cargo']


@admin.register(bateria)
class BateriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'cargo']


@admin.register(cheers)
class CheersAdmin(admin.ModelAdmin):
    list_display = ['name', 'cargo']


@admin.register(esports)
class EsportsAdmin(admin.ModelAdmin):
    list_display = ['name', 'cargo']

@admin.register(media)
class media(admin.ModelAdmin):
    list_display = ['name', 'tag']


@admin.register(competicoes)
class Competicoes(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'descricao']


@admin.register(jogos)
class Jogos(admin.ModelAdmin):
    list_display = ['time1', 'time2']
    search_fields = ['time1', 'time2']