# Generated by Django 3.0.6 on 2020-07-09 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_produtos_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Produtos', to='ecommerce.produtobase', verbose_name='Modelo'),
        ),
    ]