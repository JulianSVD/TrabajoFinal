from django.shortcuts import render
from AppPagina.models import *
from AppUsuarios.models import *


def inicio(request):
    return render (request, "AppPagina/inicio.html")
    
def blogs(request):
    posts = Post.objects.all()
    return render(request, "AppPagina/blogs.html", {"posteos": posts})


def leer_mas(request, slug):
    posts = Post.objects.get(slug=slug)
    return render(request, "AppPagina/leer_mas.html", {"posteos": posts})