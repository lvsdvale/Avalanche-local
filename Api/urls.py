from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path('EventosApi', EventosApiView.as_view(), name='EventosApi'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)