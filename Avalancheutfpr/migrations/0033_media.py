# Generated by Django 3.0.6 on 2020-06-03 07:17

import Avalancheutfpr.services
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0032_auto_20200529_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('foto', stdimage.models.StdImageField(upload_to=Avalancheutfpr.services.get_file_path)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'mídia',
                'verbose_name_plural': ' mídias',
            },
        ),
    ]
