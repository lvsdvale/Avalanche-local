# Generated by Django 3.1 on 2020-12-27 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contas', '0012_auto_20200930_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='user',
            name='data_joined',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de inscrição'),
        ),
    ]
