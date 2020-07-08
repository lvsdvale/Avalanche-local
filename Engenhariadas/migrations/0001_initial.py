# Generated by Django 3.0.6 on 2020-07-08 04:14

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
            name='engenhariadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to=Avalancheutfpr.services.get_file_path)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Data de publicação')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data de Realização')),
                ('Status', models.CharField(blank=True, choices=[('Ativo', 'Ativo'), ('Encerrado', 'Encerrado')], default='Ativo', max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Engenhariadas Paranaense',
                'verbose_name_plural': 'Engenhariadas Paranaense',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='pagamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to=Avalancheutfpr.services.get_file_path)),
                ('pagamento', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor Depositado')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data do Pagamento')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='parceladao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('cpf', models.CharField(max_length=255, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=30, verbose_name='Contato')),
                ('pagamento', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor Pago')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data da inscrição')),
                ('engenhariadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Engenhariadas.engenhariadas', verbose_name='Edição do Engenhariadas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='inscrito', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Parceladão',
                'verbose_name_plural': 'Parceladões',
                'ordering': ['engenhariadas'],
            },
        ),
    ]
