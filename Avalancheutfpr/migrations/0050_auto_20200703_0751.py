# Generated by Django 3.0.6 on 2020-07-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0049_auto_20200703_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalidades',
            name='Contatos',
            field=models.TextField(verbose_name='Contatos da Modalidade'),
        ),
    ]
