# Generated by Django 3.0.5 on 2020-05-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0004_auto_20200520_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='campanhas',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventos',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
