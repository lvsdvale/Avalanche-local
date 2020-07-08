from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('EP/', Engenhariadas.as_view(), name='Engenhariadas'),
    path('EP/<slug:slug>',EngenhariadasView,name = 'Engenhariadas_View'),

     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)