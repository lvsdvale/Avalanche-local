from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', Home.as_view(), name='Home'),
                  path('Eventos/', Eventos.as_view(), name='Eventos'),
                  path('Eventos/<slug:slug>', Eventos_view, name='Eventos_View'),
                  path('Eventos/<slug:slug>/midias', Eventos_midias, name='Eventos_Midias'),
                  path('Esportes/', Esportes.as_view(), name='Esportes'),
                  path('Esportes/<slug:slug>', Modalidades_view, name='Modalidades_View'),
                  path('Esportes/<slug:slug>/midias', Modalidades_midias, name='Modalidades_Midias'),
                  path('Contatos/', Contatos, name='Contatos'),
                  path('SobreNos/', SobreNos.as_view(), name= 'SobreNos'),
                  path('Socio/', Socio.as_view(), name='Socio'),
                  path('Social/', Social, name='Social'),
                  path('Social/<slug:slug>', Campanhas_view, name='Campanhas_View'),
                  path('Social/<slug:slug>/midias', Campanhas_midias, name='Campanhas_Midias'),
                  path('E_sports/', E_sports.as_view(), name='E-sports'),
                  path('E_sports/<slug:slug>', Games_view, name='Games_View'),
                  path('Diretoria',Diretoria,name = 'Diretoria'),
                  path('Galeria',Galeria.as_view(),name = 'Galeria'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
