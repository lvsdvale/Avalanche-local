# Generated by Django 3.0.9 on 2021-01-14 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contas', '0014_auto_20201226_2323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name'], 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Nome_completo',
            new_name='name',
        ),
    ]