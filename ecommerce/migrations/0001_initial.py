# Generated by Django 3.0.6 on 2020-07-09 12:50

import Avalancheutfpr.services
import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='produtobase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('thumb', stdimage.models.StdImageField(blank=True, null=True, upload_to=Avalancheutfpr.services.get_file_path, verbose_name='thumbnail')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('p_socio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço para Sócio')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('estoque', models.PositiveIntegerField(verbose_name='Quantidade em estoque')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('Status', models.CharField(blank=True, choices=[('Ativo', 'Ativo'), ('Encerrado', 'Encerrado')], default='Ativo', max_length=30, null=True)),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Produtos', to='ecommerce.produtobase', verbose_name='Produtos')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Pagamento Concluído'), (2, 'Entregue'), (3, 'Cancelada')], default=0, verbose_name='Status do pedido')),
                ('pagamento', models.CharField(choices=[('Deposito', 'Depósito'), ('PagSeguro', 'PagSeguro'), ('PicPay', 'PicPay')], default='Deposito', max_length=255, verbose_name='Opção de Pagamento')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='itemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade do item no carrinho')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Itens', to='ecommerce.pedidos', verbose_name='Pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.produtos', verbose_name='Produtos')),
            ],
            options={
                'verbose_name': 'item do pedido',
                'verbose_name_plural': 'itens do Pedidos',
            },
        ),
        migrations.CreateModel(
            name='itemcarrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.CharField(db_index=True, max_length=255, verbose_name='Chave do carrinho')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade do item no carrinho')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.produtos', verbose_name='Produtos')),
            ],
            options={
                'verbose_name': 'Item no carrinho',
                'verbose_name_plural': 'Itens no carrinho',
                'ordering': ['chave'],
                'unique_together': {('chave', 'produto')},
            },
        ),
    ]
