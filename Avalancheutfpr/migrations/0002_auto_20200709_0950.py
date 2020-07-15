# Generated by Django 3.0.6 on 2020-07-09 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Avalancheutfpr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao_modalidades',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='inscrito', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='inscricao_e_sports',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Avalancheutfpr.games', verbose_name='E-Modalidade'),
        ),
        migrations.AddField(
            model_name='inscricao_e_sports',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='inscrito', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='inscricao_campanhas_sociais',
            name='campanha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Avalancheutfpr.campanhas', verbose_name='Campanha'),
        ),
        migrations.AddField(
            model_name='inscricao_campanhas_sociais',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='inscrito', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]