"""Avalanche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.apps import apps



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Avalancheutfpr.urls')),
    path('',include('Blog.urls')),
    path('',include('Contas.urls')),
    path('',include('E_commerce.urls')),
    path('API/',include('Api.urls')),
    path('',include('Engenhariadas.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('painel',include('Administrativo.urls')),
    url(r'^', include(apps.get_app_config('E_commerce').urls[0])),
    path('i18n/', include('django.conf.urls.i18n')),
    path('summernote/', include('django_summernote.urls')),

    #path('', include(apps.get_app_config('oscar').urls[0])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = "A.A.A.E.A UTFPR-CT"
admin.AdminSite.site_title = "Gestão"
admin.AdminSite.index_title = "Sistema Avalanche"