from django.db import models
from stdimage.models import StdImageField
from .services import get_file_path
from autoslug import AutoSlugField
from django.conf import settings

# Classes Referentes a Página de eventos

class eventos(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'),)
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome')
    previa = models.TextField(null=False, blank=False, verbose_name='Prévia')
    descricao = models.TextField(null=False, blank=False, verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=False, blank=False)
    slug = AutoSlugField(populate_from = 'name')
    data = models.DateField(auto_now_add=False, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de Publicação')
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
    previa = models.TextField(null=False, blank=False, verbose_name='Prévia')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=False, blank=False,verbose_name="Imagem")
    logo = StdImageField(upload_to=get_file_path, null=False, blank=False,verbose_name="Logo")
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de publicação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')

    class Meta:
        verbose_name='Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ['name']

    def __str__(self):
        return self.name

class inscricaomodalidadesManager(models.Manager):
    def inscrever(self,usuario,modalidade):
        inscricao = self.create(usuario = usuario,name = usuario.name,email=usuario.email,
                                curso = usuario.Curso,Ra = usuario.Registro_Academico,
                                telefone = usuario.Telefone,modalidade=modalidade)
        inscricao.save()

class inscricao_modalidades(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_query_name='inscrito',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False,verbose_name='Nome')
    email = models.CharField(max_length=255, null=False, blank=False,verbose_name='Email')
    curso = models.CharField(max_length=255, null=False, blank=False,verbose_name='Curso')
    Ra = models.CharField(max_length=30, null=False, blank=False,verbose_name='Registro Acadêmico')
    telefone = models.CharField(max_length=30, null=False, blank=False,verbose_name='Contato')
    modalidade = models.ForeignKey(modalidades,verbose_name='Modalidade',on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, verbose_name='Data da inscrição')
    objects = inscricaomodalidadesManager()
    class Meta:
        verbose_name = 'Modalidades - inscrições'
        verbose_name_plural = 'Modalidades - inscrições'
        ordering = ['modalidade']


# Classes referentes a página de social
class campanhas(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'),)
    name = models.CharField(max_length=30,null=False,blank=False,verbose_name='Nome')
    previa = models.TextField(null=False, blank=False, verbose_name='Prévia')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    local = models.CharField(max_length=255)
    image = StdImageField(upload_to=get_file_path, null=False, blank=False)
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

class inscricaocampanhasManager(models.Manager):
    def inscrever(self,usuario,Campanha):
        inscricao = self.create(usuario = usuario,name = usuario.name,email=usuario.email,
                                curso = usuario.Curso,Ra = usuario.Registro_Academico,
                                telefone = usuario.Telefone,campanha=Campanha)
        inscricao.save()
class inscricao_campanhas_sociais(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_query_name='inscrito',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=255, null=False, blank=False, verbose_name='Email')
    curso = models.CharField(max_length=255, null=False, blank=False, verbose_name='Curso')
    Ra = models.CharField(max_length=30, null=False, blank=False, verbose_name='Registro Acadêmico')
    telefone = models.CharField(max_length=30, null=False, blank=False, verbose_name='Contato')
    campanha = models.ForeignKey(campanhas, verbose_name='Campanha', on_delete=models.CASCADE)
    Compareceu = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True,verbose_name='Data da inscrição')
    objects = inscricaocampanhasManager()
    class Meta:
        verbose_name = 'Ações Sociais - inscrições'
        verbose_name_plural = 'Ações Sociais - inscrições'
        ordering = ['campanha']


# classes da página de e-sports
class games(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'))
    name = models.CharField(max_length=30,null=False,blank=False,verbose_name='Nome')
    previa = models.TextField(null=False, blank=False, verbose_name='Prévia')
    descricao = models.TextField(null=False,blank=False,verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=False, blank=False)
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

class inscricaoEsportsManager(models.Manager):
    def inscrever(self,usuario,game):
        inscricao = self.create(usuario = usuario,name = usuario.name,email=usuario.email,
                                curso = usuario.Curso,Ra = usuario.Registro_Academico,
                                telefone = usuario.Telefone,game=game)
        inscricao.save()

class inscricao_E_sports(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_query_name='inscrito',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=255, null=False, blank=False, verbose_name='Email')
    curso = models.CharField(max_length=255, null=False, blank=False, verbose_name='Curso')
    Ra = models.CharField(max_length=30, null=False, blank=False, verbose_name='Registro Acadêmico')
    telefone = models.CharField(max_length=30, null=False, blank=False, verbose_name='Contato')
    game = models.ForeignKey(games, verbose_name='E-Modalidade', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, verbose_name='Data da inscrição')
    objects = inscricaoEsportsManager()
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
    Cargos = (
        (1, "Presidente"),
        (2, "Vice Presidente"),
        (3, "Diretor Geral"),
        (4, "Diretor de Esportes"),
        (5, "Diretora de Esportes"),
        (6, "Assessora de Esportes "),
        (7, "Assessor de Esportes"),
        (8, "Diretor de Eventos"),
        (9, "Diretora de Eventos"),
        (10, "Coordenadora de Eventos"),
        (11, "Coordenador de Eventos"),
        (12, "Assessor de Eventos"),
        (13, "Assessora de Eventos"),
        (14, "Diretor de Responsabilidade Social"),
        (15, "Diretora de Responsabilidade Social"),
        (16, "Assesora de Responsabilidade Social"),
        (17, "Assesor de Responsabilidade Social"),
        (18, "Diretor de Marketing"),
        (19, "Diretora de Marketing"),
        (20, "Assessora de Marketing"),
        (21, "Assessor de Marketing"),
        (22, "Diretor Administrativo"),
        (23, "Diretora Administrativo"),
        (24, "Coordenador Administrativo"),
        (25, "Coordenadora Administrativa"),
        (26, "Assessor Administrativo"),
        (27, "Assessora  Administrativa"),
        (28, "Diretor de Relaçoes institucionais"),
        (29, "Diretora de Relaçoes institucionais"),
        (30, "Assessora de Relaçoes institucionais"),
        (31, "Assessor de Relaçoes institucionais"),
        (32, "Diretor de TI"),
    )
    name = models.CharField(max_length=255,null=False,blank=False,unique=True,verbose_name='Nome')
    cargo = models.IntegerField(choices=Cargos,null=False,blank=False,verbose_name='Cargo')
    foto = StdImageField(upload_to=get_file_path,null = False,blank = False)
    instagram = models.CharField(max_length=255,null=True,blank=True,verbose_name='Instagram')
    facebook =  models.CharField(max_length=255,null=True,blank=True,verbose_name='Facebook')
    def retorna_cargo(self):
        return self.cargo
    class Meta:
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'
        ordering = ['cargo']

    def __str__(self):
        return self.name

class cheers(models.Model):
    Cargos = (
        (1,"Presidente"),
        (2,"Secretária"),
        (3,"Tesoureira"),
        (4,"Diretora de Marketing"),
        (5,"Capitão"),
    )
    name = models.CharField(max_length=255,null=False,blank=False,unique=True,verbose_name='Nome')
    cargo = models.IntegerField(choices=Cargos,null=False,blank=False,verbose_name='Cargo')
    foto = StdImageField(upload_to=get_file_path,null = False,blank = False)
    instagram = models.CharField(max_length=255,null=True,blank=True,verbose_name='Instagram')
    facebook =  models.CharField(max_length=255,null=True,blank=True,verbose_name='Facebook')
    def retorna_cargo(self):
        return self.cargo
    class Meta:
        verbose_name = 'Direção Cheers'
        verbose_name_plural = 'Direção Cheers'
        ordering = ['cargo']


class bateria(models.Model):
    Cargos = (
        (1, "Presidente"),
        (2, "Vice Presidente"),
        (3, "Mestre"),
        (4, "Marketing"),
        (5, "Financeiro"),
        (6, "Produtos"),
        (7, "Materiais"),
    )
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Nome')
    cargo = models.IntegerField(choices=Cargos, null=False, blank=False, verbose_name='Cargo')
    foto = StdImageField(upload_to=get_file_path, null=False, blank=False)
    instagram = models.CharField(max_length=255, null=True, blank=True, verbose_name='Instagram')
    facebook = models.CharField(max_length=255, null=True, blank=True, verbose_name='Facebook')

    def retorna_cargo(self):
        return self.cargo

    class Meta:
        verbose_name = 'Direção Bateria'
        verbose_name_plural = 'Direção Bateria'
        ordering = ['cargo']

class esports(models.Model):
    Cargos = (
        (1, "Presidente"),
        (2, "Diretor de Comunicação"),
        (3, "Diretor de Comunicação"),
        (4, "Diretor de Esports"),
        (5, "Diretora de Esports"),
        (6,"Manager de Esports"),
        (7, "Diretora Financeira"),
        (8, "Diretor Financeiro"),
        (9,"Secretário"),
        (10, "Secretária"),
        (11,"Diretor de Patrocínios"),
        (12, "Diretora de Patrocínios"),
        (13,"Manager de Produtos"),
        (14, "Diretor de Saúde"),
        (15, "Diretora de Saúde"),
        (16, "Coordenador de Psicologia"),
        (17, "Coordenadora de Psicologia"),
        (18, "Psicólogo"),
        (19, "Psicóloga"),
        (20, "Diretor de Torneios"),
        (21, "Diretora de Torneios"),
        (22, "Manager Torneios"),
        (23, "Social Media"),
        (24, "Redator"),
        (25, "Redatora"),
        (26, "Editora de Vídeo"),
        (27, "Editor de Vídeo"),
        (28, "Motion Designer"),
        (29, "Designer"),
        (30,"Ilustrador"),
        (31,"Ilustradora"),

    )
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Nome')
    cargo = models.IntegerField(choices=Cargos, null=False, blank=False, verbose_name='Cargo')
    foto = StdImageField(upload_to=get_file_path, null=False, blank=False)
    instagram = models.CharField(max_length=255, null=True, blank=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=255, null=True, blank=True, verbose_name='twitter')

    def retorna_cargo(self):
        return self.cargo

    class Meta:
        verbose_name = 'Direção Esports'
        verbose_name_plural = 'Direção Esports'
        ordering = ['cargo']

class media(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,verbose_name='Nome')
    tag = models.CharField(max_length=255,null=False,blank=False)
    foto = StdImageField(upload_to=get_file_path, null=False, blank=False)
    video = models.FileField(upload_to=get_file_path,null=True, blank=True)
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de Criação')
    class Meta:
        verbose_name =  'mídia'
        verbose_name_plural = ' mídias'
        ordering = ['tag']
    def __str__(self):
        return self.name

class competicoes(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'))
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome')
    previa = models.TextField(null=False, blank=False, verbose_name='Prévia')
    descricao = models.TextField(null=False, blank=False, verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=False, blank=False)
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de publicação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')
    class Meta:
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'
        ordering = ['name']

    def __str__(self):
        return self.name
class jogos(models.Model):
    competicao = models.ForeignKey(competicoes,verbose_name="Competição",on_delete=models.CASCADE)
    time1 = models.CharField(max_length=300,null=False,blank=False,verbose_name="Time da casa")
    time2 = models.CharField(max_length=300,null=False,blank=False,verbose_name="Time visitante")
    imgtime1= StdImageField(upload_to=get_file_path, null=True, blank=True,verbose_name="Logotipo time da casa")
    imgtime2= StdImageField(upload_to=get_file_path, null=True, blank=True,verbose_name="logotipo time visitante")
    placart1 = models.IntegerField(null=False,blank=False,verbose_name="Pontos do time da casa")
    placart2 = models.IntegerField(null=False,blank=False,verbose_name="Pontos do time visitante")
    horario = models.TimeField(auto_now_add=True,verbose_name="Horário do jogo")
    local = models.CharField(max_length=300,blank=True,null=False,verbose_name="Local")
    data = models.DateField(auto_now_add=True,verbose_name='Data do jogo')
    def __str__(self):
        return f'{self.time1} X {self.time2}'
    class Meta:
        verbose_name =  'Jogo'
        verbose_name_plural = 'Jogos'

class lance(models.Model):
    jogo = models.ForeignKey(jogos, verbose_name="Jogo", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=300,blank=False,null=False,verbose_name="Titulo da jogada")
    descricao = models.CharField(max_length=300,null=False,blank=False,verbose_name="Descrição do Lance")
    tempo = models.TimeField(auto_now_add=True,verbose_name="Tempo")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Lance'
        verbose_name_plural = 'Lance'


class album(models.Model):
    titulo = models.CharField(max_length=250,verbose_name = "Titulo")
    slug = AutoSlugField(populate_from='titulo')
    capa = models.FileField(blank=True, verbose_name = "Capa")
    data = models.DateField(auto_now_add=True, verbose_name='Data')
    def __str__(self):
        return self.titulo


    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'


class fotos(models.Model):
    album = models.ForeignKey(album, default=None,related_name="album", on_delete=models.CASCADE)
    foto = models.ImageField(upload_to=get_file_path, verbose_name= 'Foto')
    def __str__(self):
        return f'{self.album.titulo} - foto{self.id}'

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'