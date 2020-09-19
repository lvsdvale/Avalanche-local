# Generated by Django 3.1.1 on 2020-09-19 05:10

import Avalancheutfpr.services
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome da categoria')),
            ],
            options={
                'verbose_name': 'Categoria de Documentos',
                'verbose_name_plural': 'Categorias de Documentos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome')),
                ('arquivo', models.FileField(upload_to=Avalancheutfpr.services.get_file_path, verbose_name='Arquivo')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Documento', to='Administrativo.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'ordering': ['name'],
            },
        ),
    ]
