# Generated by Django 3.0.5 on 2020-05-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0018_auto_20200522_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao_esportes',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
