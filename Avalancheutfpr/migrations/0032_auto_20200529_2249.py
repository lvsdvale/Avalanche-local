# Generated by Django 3.0.5 on 2020-05-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0031_diretoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretoria',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='diretoria',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
