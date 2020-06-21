from django.db import models
from stdimage.models import StdImageField
from .services import get_file_path
from autoslug import AutoSlugField
from django.conf import settings

# Classes Referentes a Página de eventos

class eventos(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'),)
    name = models.CharField(max_length=30,null=False,blank=False,verbose_name='Nome')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True)
    QRcode = StdImageField(upload_to=get_file_path,null = True, blank= True)
    slug = AutoSlugField(populate_from = 'name')
    data = models.DateField(auto_now_add=False,blank=True,null=True)
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de Publicação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')


    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-pub_date']


    def __str__(self):
        return self.name


# classes referentes a página de Esportes
class modalidades(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'),)
    name = models.CharField(max_length=30,null=False,blank=False,verbose_name='Nome')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    Contatos = models.TextField(default="Diretoria@atleticautfpr.com.br")
    image = StdImageField(upload_to=get_file_path, null=True, blank=True)
    QRcode = StdImageField(upload_to=get_file_path,null = True, blank = True)
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de publicação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')

    class Meta:
        verbose_name='Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ['name']

    def __str__(self):
        return self.name


class inscricao_modalidades(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Usuário',on_delete=models.CASCADE)
    modalidade = models.ForeignKey(modalidades,verbose_name='Modalidade',on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, verbose_name='Data da inscrição')
    class Meta:
        verbose_name = 'Modalidades - inscrições'
        verbose_name_plural = 'Modalidades - inscrições'
        ordering = ['modalidade']


# Classes referentes a página de social
class campanhas(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'),)
    name = models.CharField(max_length=30,null=False,blank=False,verbose_name='Nome')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    local = models.CharField(max_length=255)
    image = StdImageField(upload_to=get_file_path, null=True, blank=True)
    QRcode = StdImageField(upload_to=get_file_path, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    data = models.DateField(auto_now_add=False, blank=True, null=True,verbose_name='Data de Realização')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de publicação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')


    class Meta:
        verbose_name= 'Ação Social'
        verbose_name_plural = 'Ações Sociais'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class inscricao_campanhas_sociais(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    campanha = models.ForeignKey(campanhas, verbose_name='Campanha', on_delete=models.CASCADE)
    Compareceu = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True,verbose_name='Data da inscrição')

    class Meta:
        verbose_name = 'Ações Sociais - inscrições'
        verbose_name_plural = 'Ações Sociais - inscrições'
        ordering = ['campanha']


# classes da página de e-sports
class games(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'))
    name = models.CharField(max_length=30,null=False,blank=False,verbose_name='Nome')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True)
    QRcode = StdImageField(upload_to=get_file_path, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de publicação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')

    class Meta:
        verbose_name = 'Modalidade de E-sports'
        verbose_name_plural = 'Modalidades de E-sports'
        ordering = ['name']

    def __str__(self):
        return self.name


class inscricao_E_sports(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    game = models.ForeignKey(games, verbose_name='E-Modalidade', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, verbose_name='Data da inscrição')

    class Meta:
        verbose_name = 'E-sports - inscrições'
        verbose_name_plural = 'E-sports - inscrições'
        ordering = ['game']

#Classe de Contatos
class contatos(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False,verbose_name='Nome')
    email = models.CharField(max_length=255, null=False, blank=False)
    assunto = models.CharField(max_length=255, null=False, blank=False)
    mensagem = models.TextField(max_length=500,null = False,blank=False)
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data do contato')
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-pub_date']
    def __str__(self):
        return self.name
class diretoria(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,unique=True,verbose_name='Nome')
    area = models.CharField(max_length=255,null=True,blank=True,verbose_name='Area')
    foto = StdImageField(upload_to=get_file_path,null = False,blank = False)
    video = models.FileField(upload_to=get_file_path,null=True,blank=True)

    class Meta:
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'
        ordering = ['area']

    def __str__(self):
        return self.name
class inscricao_processo_seletivo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    Areas = models.CharField(max_length=255, null=True, blank=True,help_text='Coloque as areas que deseja participar')
    class Meta:
        verbose_name = 'Processo Seletivo'
        verbose_name_plural = 'Processo Seletivo'
    def __str__(self):
        return self.Areas
class media(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,verbose_name='Nome')
    tag = models.CharField(max_length=255,null=False,blank=False)
    foto = StdImageField(upload_to=get_file_path, null=False, blank=False)
    video = models.FileField(upload_to=get_file_path,null=True, blank=True)

    class Meta:
        verbose_name =  'mídia'
        verbose_name_plural = ' mídias'
        ordering = ['tag']
    def __str__(self):
        return self.name

