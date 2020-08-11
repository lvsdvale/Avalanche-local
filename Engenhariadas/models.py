from django.db import models
from autoslug import AutoSlugField
from Avalancheutfpr.services import get_file_path
from stdimage import StdImageField
from django.conf import settings
from picpay import PicPay

class engenhariadas(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'))
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    descricao = models.TextField(null=False, blank=False, verbose_name='Descrição')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de publicação')
    data = models.DateField(auto_now_add=False, blank=True, null=True, verbose_name='Data de Realização')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')
    class Meta:
        verbose_name= 'Engenhariadas Paranaense'
        verbose_name_plural = 'Engenhariadas Paranaense'
        ordering = ['-pub_date']
    def __str__(self):
        return self.name
class parceladaoMenager(models.Manager):
    def inscrever(self,usuario,engenhariadas):
        Parceladao = self.create(usuario=usuario,name = usuario.Nome_completo,email = usuario.email,cpf = usuario.CPF,
                                telefone = usuario.telefone,engenhariadas = engenhariadas)
        Parceladao.save()
class parceladao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_query_name='inscrito',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=255, null=False, blank=False, verbose_name='Email')
    cpf = models.CharField(max_length=255, null=False, blank=False, verbose_name='CPF')
    telefone = models.CharField(max_length=30, null=False, blank=False, verbose_name='Contato')
    engenhariadas = models.ForeignKey(engenhariadas, verbose_name='Edição do Engenhariadas',related_name='EP', on_delete=models.CASCADE)
    pagamento = models.DecimalField(decimal_places=2,max_digits=6,verbose_name='Valor Pago')
    data = models.DateField(auto_now_add=True,verbose_name='Data da inscrição')
    objects = parceladaoMenager()

    class Meta:
        verbose_name = 'Parceladão'
        verbose_name_plural = 'Parceladões'
        ordering = ['engenhariadas']

class pagamentoMenager(models.Manager):
    def adicionar(self,usuario):
        Pagamento = self.create(usuario=usuario,name = usuario.Nome_completo,email = usuario.email,
                                telefone = usuario.telefone)
        Pagamento.save()
class pagamentos(models.Model):
    PAGAMENTO_CHOICES = (
        ('Deposito', 'Depósito'),
        ('PicPay', 'PicPay'),
        ('Presencial', 'Presencial'),
    )
    STATUS_CHOICES = (
        (0, 'Aguardando Validação'),
        (1, 'Pagamento Validado'),
    )
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_query_name='inscrito',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=255, null=False, blank=False, verbose_name='Email')
    image = StdImageField(upload_to=get_file_path, null=True, blank=True,verbose_name='Comprovante de Pagamento',
                          help_text='Caso o pagamento for via DEPOSITO NA CONTA DA CAIXA enviar imagem do comprovante de pagamento')
    deposito = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor Depositado')
    pagamento = models.CharField(max_length=255,choices=PAGAMENTO_CHOICES,blank=False,null=False,
                                             verbose_name='Opção de Pagamento',default='Deposito')
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='Status da Validação', default=0)
    data = models.DateField(auto_now_add=True, verbose_name='Data do Pagamento')
    objects = pagamentoMenager()

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['data']

    def Adicionar_Valor(self,Parceladao):
        if self.status == 1:
            if Parceladao.engenhariadas.status == 'Ativo':
                Parceladao.pagamento = Parceladao.pagamento + self.deposito
                Parceladao.save()
    def picpay_update_status(self, status):
        if status == 'paid':
            self.status = 1
        self.save()
    def picpay(self):
        self.pagamento = 'PicPay'
        self.save()
        pc = PicPay(
            x_picpay_token=settings.X_PICPAY_TOKEN, x_seller_token=settings.X_SELLER_TOKEN
        )
        return pc
    def __str__(self):
        self.name