# Generated by Django 4.1.3 on 2023-01-20 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppPagina', '0003_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
