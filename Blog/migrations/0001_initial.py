# Generated by Django 3.0.6 on 2020-07-09 12:50

import Avalancheutfpr.services
import autoslug.fields
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to=Avalancheutfpr.services.get_file_path, verbose_name='imagem')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Data de Publicação')),
            ],
            options={
                'verbose_name': 'Post Blog',
                'verbose_name_plural': 'Posts Blog',
            },
        ),
    ]
