# Generated by Django 3.0.6 on 2020-06-09 16:15

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avalancheutfpr', '0039_auto_20200609_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='padrao', editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
