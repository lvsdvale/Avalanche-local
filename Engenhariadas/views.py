from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import View,TemplateView,FormView,ListView

# Create your views here.
    name = models.CharField(max_length=30,null = False,blank=False,verbose_name='Nome')
    conteudo = models.TextField(null=False,blank=False,verbose_name='Conteúdo')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True,verbose_name='imagem')
    slug = AutoSlugField(populate_from = 'name')
    ativo = ()
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de Publicação')
