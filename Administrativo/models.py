from django.db import models
from Avalancheutfpr.services import get_file_path
class categoria(models.Model):
    name = models.CharField(max_length=250,null=False,blank=False,verbose_name="Nome da categoria")
    class Meta:
        verbose_name = 'Categoria de Documentos'
        verbose_name_plural = 'Categorias de Documentos'
        ordering = ['name']

class documento(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name="Nome")
    categoria = models.ForeignKey(categoria, verbose_name='Categoria',null=True,
                               related_name='Documento',on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to=get_file_path,null=False,blank=False,verbose_name="Arquivo")
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['name']
