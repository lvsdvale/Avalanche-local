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

class custo(models.Model):
    name = models.CharField(max_length=250,null=False,blank=False,verbose_name="Nome")
    class Meta:
        verbose_name = 'Centro de custo'
        verbose_name_plural = 'Centros de custo'
        ordering = ['name']

class contaspagar(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name="Título")
    data = models.DateField(auto_now_add=True,verbose_name="Data de Vencimento")
    fornecedor = models.CharField(max_length=255,null=False,blank=False,verbose_name="Fornecedor")
    valor = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor do título")
    juros = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Juros")
    barras = models.IntegerField(verbose_name="Código de Barras")
    Custo = models.ForeignKey(custo, verbose_name='Centro de custo',null=True,
                               related_name='Pagar',on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to=get_file_path,null=False,blank=True,verbose_name="Nota")
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    class Meta:
        verbose_name = 'Conta a pagar'
        verbose_name_plural = 'Contas a pagar'
        ordering = ['name']

class contasreceber(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name="Título")
    data = models.DateField(auto_now_add=True,verbose_name="Data do recebimento")
    valor = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor do título")
    juros = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Juros")
    Custo = models.ForeignKey(custo, verbose_name='Centro de custo',null=True,
                               related_name='Receber',on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to=get_file_path,null=False,blank=True,verbose_name="Nota")
    pub_date = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    class Meta:
        verbose_name = 'Conta a receber'
        verbose_name_plural = 'Contas a receber'
        ordering = ['name']