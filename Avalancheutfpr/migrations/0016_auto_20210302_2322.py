# Generated by Django 3.0.9 on 2021-03-03 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0015_auto_20210220_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretoria',
            name='cargo',
            field=models.IntegerField(choices=[(1, 'Presidente'), (2, 'Vice Presidente'), (3, 'Diretor Geral'), (4, 'Diretor de Esportes'), (5, 'Diretora de Esportes'), (6, 'Assessora de Esportes '), (7, 'Assessor de Esportes'), (8, 'Diretor de Eventos'), (9, 'Diretora de Eventos'), (10, 'Coordenadora de Eventos'), (11, 'Coordenador de Eventos'), (12, 'Assessor de Eventos'), (13, 'Assessora de Eventos'), (14, 'Diretor de Responsabilidade Social'), (15, 'Diretora de Responsabilidade Social'), (16, 'Assesora de Responsabilidade Social'), (17, 'Assesor de Responsabilidade Social'), (18, 'Diretor de Marketing'), (19, 'Diretora de Marketing'), (20, 'Assessora de Marketing'), (21, 'Assessor de Marketing'), (22, 'Diretor Administrativo'), (23, 'Diretora Administrativo'), (24, 'Coordenador Administrativo'), (25, 'Coordenadora Administrativa'), (26, 'Assessor Administrativo'), (27, 'Assessora  Administrativa'), (28, 'Diretor de Relaçoes institucionais'), (29, 'Diretora de Relaçoes institucionais'), (30, 'Assessora de Relaçoes institucionais'), (31, 'Assessor de Relaçoes institucionais'), (32, 'Diretor de TI')], verbose_name='Cargo'),
        ),
    ]