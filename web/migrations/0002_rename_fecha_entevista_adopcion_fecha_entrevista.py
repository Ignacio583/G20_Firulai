# Generated by Django 5.0.6 on 2024-07-01 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopcion',
            old_name='fecha_entevista',
            new_name='fecha_entrevista',
        ),
    ]
