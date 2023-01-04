from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
"""
class UsuarioForm(UserCreationForm):
    name=forms.CharField(label="name", max_length=20)
    email=forms.EmailField(label="email", max_length=30)
    password=forms.CharField(label="password", max_length=30)
"""

class UsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields} #Para borrar las sugerencias