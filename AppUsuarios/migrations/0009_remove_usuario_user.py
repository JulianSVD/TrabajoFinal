# Generated by Django 4.1.3 on 2023-01-20 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0008_usuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
    ]
