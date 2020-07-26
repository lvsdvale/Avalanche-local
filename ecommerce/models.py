from django.db import models
from stdimage.models import StdImageField
from Avalancheutfpr.services import get_file_path
from autoslug import AutoSlugField
from django.conf import settings
from pagseguro import PagSeguro
from picpay import PicPay

class produtobase(models.Model):
    Destaque = (('Sim', 'Sim'), ('Não', 'Não'),)
    name = models.CharField(max_length=255,null = False,blank = False,verbose_name='Nome')
    descricao = models.TextField(null = False,blank = False,verbose_name='Descrição')
    thumb = StdImageField(upload_to=get_file_path, null=False, blank=False, verbose_name='thumbnail')
    preco = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')
    p_socio = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço para Sócio')
    destaque =  models.CharField(max_length=30, null=True, blank=True, choices=Destaque, default='Não')
    slug = AutoSlugField(populate_from='name')
    class Meta:
        verbose_name = 'Produto Base'
        verbose_name_plural = 'Produtos Base'
        ordering = ['name']
    def get_p_socio(self):
        return self.p_socio

    def get_produto(self):
        return self.Produtos.all()

    def __str__(self):
        return self.name


class produtos(models.Model):
    status = (('Ativo', 'Ativo'), ('Encerrado', 'Encerrado'),)
    modelo = models.ForeignKey(produtobase, verbose_name='Base',null=True,
                               related_name='Produtos',related_query_name='Produtos_Query',on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null = False,blank = False,verbose_name='Nome')
    estoque = models.PositiveIntegerField(verbose_name='Quantidade em estoque')
    pub_date = models.DateField(auto_now_add=True,verbose_name='Data de Criação')
    Status = models.CharField(max_length=30, null=True, blank=True, choices=status, default='Ativo')
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ['name']

    def __str__(self):
        return f'{self.modelo.name}-{self.name}'

    def set_compra(self,quantidade):
        self.estoque = self.estoque - quantidade
        self.save()

    def Esgotado(self):
        if self.estoque == 0:
            self.status = 'Encerrado'

class gerenciadoritemcarrinho(models.Manager):
    def adicionar(self,chave,produto):
        if self.filter(chave = chave,produto = produto).exists():
            criado = False
            item = self.get(chave = chave,produto = produto)
            item.quantidade = item.quantidade + 1
            item.save()
        else:
            criado = True
            item = itemcarrinho.objects.create(chave = chave,produto=produto,preco = produto.modelo.preco)
        return item,criado
    def adicionar_socio(self,chave,produto):
        if self.filter(chave = chave,produto =produto).exists():
            criado = False
            item = self.get(chave = chave,produto = produto)
            item.quantidade = item.quantidade + 1
            item.save()
        else:
            criado = True
            item = itemcarrinho.objects.create(chave = chave,produto=produto,preco = produto.modelo.p_socio)
        return item,criado

    def get_produto_p_socio(self):
        return self.produto.modelo.get_p_socio()

class itemcarrinho(models.Model):
    chave = models.CharField(max_length=255,verbose_name='Chave do carrinho',db_index=True)
    produto = models.ForeignKey(produtos,verbose_name='Produtos',on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade do item no carrinho',default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')
    objects = gerenciadoritemcarrinho()
    class Meta:
        verbose_name = 'Item no carrinho'
        verbose_name_plural = 'Itens no carrinho'
        ordering = ['chave']
        unique_together = (('chave','produto'),)
    def __str__(self):
        return f'{self.produto} {self.quantidade}'

class pedidosmanager(models.Manager):
    def adicionar(self,usuario,itenscarrinho):
        pedido = self.create(usuario=usuario)
        for item in itenscarrinho:
            item_pedido = itemPedido.objects.create(pedido = pedido,
                                                    quantidade = item.quantidade,
                                                    produto = item.produto,
                                                    preco = item.preco
                                                    )
        return pedido



class pedidos(models.Model):
    STATUS_CHOICES = (
        (0,'Aguardando Pagamento'),
        (1,'Pagamento Concluído'),
        (2,'Entregue'),
        (3,'Cancelada'),
    )
    PAGAMENTO_CHOICES = (
        ('Deposito','Depósito'),
        ('PagSeguro','PagSeguro'),
        ('PicPay','PicPay'),
    )
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Usuário',on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES,verbose_name='Status do pedido',default=0,blank=True)
    pagamento = models.CharField(max_length=255,choices=PAGAMENTO_CHOICES,blank=False,null=False,verbose_name='Opção de Pagamento',default='Deposito')
    criado = models.DateField(auto_now_add=True,verbose_name='Data de criação')
    objects = pedidosmanager()
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    def __str__(self):
        return f'pedido {self.pk}'
    def produto(self):
        Produtos_ids = self.Itens.values_list('produto')
        return produtos.objects.filter(pk__in = Produtos_ids)
    def total(self):
        aggregate_queryset = self.Itens.aggregate(total = models.Sum(models.F('preco')*models.F('quantidade'),output_field =models.DecimalField()))
        return aggregate_queryset['total']

    def pagseguro_update_status(self, status):
        if status == '3':
            self.status = 1
        elif status == '7':
            self.status = 3
        self.save()
    def complete(self):
        self.status = 2
        self.save()

    def pagseguro(self):
        self.pagamento = 'PagSeguro'
        self.save()
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        pg.sender = {
            'email': self.usuario.email
        }
        pg.reference_prefix = None
        pg.shipping = None
        pg.reference = self.pk
        for item in self.Itens.all():
            pg.items.append(
                {
                    'id': item.produto.pk,
                    'description': item.produto,
                    'amount': '%.2f' % item.preco,
                    'quantity': item.quantidade,

                }
            )

        return pg

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


class itemPedido(models.Model):
    pedido = models.ForeignKey(pedidos,verbose_name='Pedido',related_name='Itens',on_delete=models.CASCADE)
    produto = models.ForeignKey(produtos, verbose_name='Produtos', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade do item no carrinho', default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')
    class Meta:
        verbose_name = 'item do pedido'
        verbose_name_plural = 'itens do Pedidos'

    def __str__(self):
        return f'[{self.pedido}] - {self.produto}'

