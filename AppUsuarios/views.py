from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from AppUsuarios.forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from AppPagina.models import *

# Create your views here.


#Vista de registro
def register(request):
    if request.method=="POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppPagina/inicio.html", {"mensaje": f"Usuario {username} creado con exito!"})
        else:
            return render(request, "AppPagina/register.html", {"form": form, "mensaje":"Error al crear usuario"})
    else:
        form = UsuarioForm()
        return render(request, "AppPagina/register.html", {"form": form})

#Vista de Login
def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppPagina/inicio.html", {"mensaje": f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppPagina/inicio.html", {"mensaje": "Usuario o contraseña No se encuentra"})
        else:
            return render(request,"AppPagina/login.html", {"form": form, "mensaje" : "Usuario o contraseña incorrectos."})
    else:
        form=AuthenticationForm()
        return render(request,"AppPagina/login.html", {"form", form})

@login_required
def editarperfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppPagina/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppPagina/editarperfil.html", {"form": form, "nombreusuario":usuario.username} )
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppPagina/editarperfil.html", {"form": form})