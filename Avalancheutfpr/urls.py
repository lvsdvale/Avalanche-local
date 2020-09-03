from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', Home.as_view(), name='Home'),
                  path('Eventos/', Eventos.as_view(), name='Eventos'),
                  path('Eventos/<slug:slug>', Eventos_view, name='Eventos_View'),
                  path('Esportes/', Esportes.as_view(), name='Esportes'),
                  path('Esportes/<slug:slug>', Modalidades_view, name='Modalidades_View'),
                  path('Contatos/', Contatos, name='Contatos'),
                  path('SobreNos/', SobreNos.as_view(), name= 'SobreNos'),
                  path('Socio/', Socio.as_view(), name='Socio'),
                  path('Social/', Social.as_view(), name='Social'),
                  path('Social/<slug:slug>', Campanhas_view, name='Campanhas_View'),
                  path('E_sports/', E_sports.as_view(), name='E-sports'),
                  path('E_sports/<slug:slug>', Games_view, name='Games_View'),
                  path('Diretoria/',Diretoria,name = 'Diretoria'),
                  path('Galeria/',Galeria.as_view(),name = 'Galeria'),
                  path('Competicoes/',Competicoes.as_view(),name = 'Competicoes')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
