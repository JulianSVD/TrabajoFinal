from django.db import models

class Usuario(models.Model):
    def __str__(self):
        return f"Usuario {self.name} - {self.email}"

    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
