from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    def __str__(self):
        return f"Usuario {self.name} - {self.email}"

    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)