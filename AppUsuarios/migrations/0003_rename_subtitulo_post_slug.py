# Generated by Django 4.1.3 on 2023-01-04 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subtitulo',
            new_name='slug',
        ),
    ]