from django.db import models
from stdimage.models import StdImageField
from autoslug import AutoSlugField
from Avalancheutfpr.services import get_file_path
class posts(models.Model):
    name = models.CharField(max_length=30,null = False,blank=False,verbose_name='Nome')
    previa = models.TextField(null=False, blank=False, verbose_name='Prévia')
    conteudo = models.TextField(null=False,blank=False,verbose_name='Conteúdo')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True,verbose_name='imagem')
    slug = AutoSlugField(populate_from = 'name')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de Publicação')

    class Meta:
        verbose_name = 'Post Blog'
        verbose_name_plural = 'Posts Blog'


    def __str__(self):
        return self.name
