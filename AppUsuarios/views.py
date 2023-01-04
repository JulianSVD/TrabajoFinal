from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from AppUsuarios.forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
"""
def register(request):
    form= UsuarioForm(request.POST)
    if request.method=="POST":
        form= UsuarioForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            name= informacion["name"]
            email= informacion["email"]
            password= informacion["password"]
            usuario = Usuario(name=name, email=email, password=password)
            usuario.save()
            return render(request, "AppPagina/inicio.html", {"mensaje": "Usuario guardado correctamente!"})
        else:
            return render(request, "AppPagina/inicio.html", {"mensaje": "Informacion NO valida"})
    else:
        form: UsuarioForm()
        return render(request, "AppPagina/register.html", {"form": form})
"""
#REVISAR ESTO, PROBABLEMENTE ERRORES!

#Vista de registro

def register(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppPagina/inicio.html", {"mensaje": f"Usuario {username} creado con exito!"})
        else:
            return render(request, "AppPagina/register.html", {"form": form, "mensaje":"Error al crear usuario"})
    else:
        form=UserCreationForm()
        return render(request, "AppPagina/register.html", {"form": form})