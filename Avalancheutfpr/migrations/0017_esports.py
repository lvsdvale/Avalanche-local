# Generated by Django 3.0.9 on 2021-03-31 05:36

import Avalancheutfpr.services
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0016_auto_20210302_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='esports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nome')),
                ('cargo', models.IntegerField(choices=[(1, 'Presidente'), (2, 'Diretor de Comunicação'), (3, 'Diretor de Comunicação'), (4, 'Diretor de Esports'), (5, 'Diretora de Esports'), (6, 'Manager de Esports'), (7, 'Diretora Financeira'), (8, 'Diretor Financeiro'), (9, 'Secretário'), (10, 'Secretária'), (11, 'Diretor de Patrocínios'), (12, 'Diretora de Patrocínios'), (13, 'Manager de Produtos'), (14, 'Diretor de Saúde'), (15, 'Diretora de Saúde'), (16, 'Coordenador de Psicologia'), (17, 'Coordenadora de Psicologia'), (18, 'Psicólogo'), (19, 'Psicóloga'), (20, 'Diretor de Torneios'), (21, 'Diretora de Torneios'), (22, 'Manager Torneios'), (23, 'Social Media'), (24, 'Redator'), (25, 'Redatora'), (26, 'Editora de Vídeo'), (27, 'Editor de Vídeo'), (28, 'Motion Designer'), (29, 'Designer'), (30, 'Ilustrador'), (31, 'Ilustradora')], verbose_name='Cargo')),
                ('foto', stdimage.models.StdImageField(upload_to=Avalancheutfpr.services.get_file_path)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='twitter')),
            ],
            options={
                'verbose_name': 'Direção Esports',
                'verbose_name_plural': 'Direção Esports',
                'ordering': ['cargo'],
            },
        ),
    ]