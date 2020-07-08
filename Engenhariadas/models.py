from django.db import models
from autoslug import AutoSlugField
from Avalancheutfpr.services import get_file_path
# Create your models here.
class engenhariadas(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'))
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome')
    descricao = models.TextField(null=False, blank=False, verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de publicação')
    data = models.DateField(auto_now_add=False, blank=True, null=True, verbose_name='Data de Realização')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')