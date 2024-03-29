# Generated by Django 3.0.6 on 2020-09-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0007_competicoes_jogos_lance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diretoria',
            options={'ordering': ['cargo'], 'verbose_name': 'Diretor', 'verbose_name_plural': 'Diretores'},
        ),
        migrations.AlterField(
            model_name='diretoria',
            name='cargo',
            field=models.CharField(choices=[(1, 'Presidente'), (2, 'Vice Presidente'), (3, 'Diretor Geral')], default=1, max_length=255, verbose_name='Cargo'),
            preserve_default=False,
        ),
    ]
