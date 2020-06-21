from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
            path('Blog/',Blog,name = 'Blog'),
            path('Blog/<slug:slug>',Post_view.as_view(),name ='Post_view')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)