# Generated by Django 3.0.6 on 2020-07-09 13:05

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
