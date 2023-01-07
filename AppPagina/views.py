from django.shortcuts import render
from AppPagina.models import *
from AppUsuarios.models import *
from AppPagina.forms import PostForm


def inicio(request):
    return render (request, "AppPagina/inicio.html")
    
def blogs(request):
    posts = Post.objects.all()
    return render(request, "AppPagina/blogs.html", {"posteos": posts})


def leer_mas(request, slug):
    posts = Post.objects.get(slug=slug)
    return render(request, "AppPagina/leer_mas.html", {"posteos": posts})

def BlogFormulario(request):
    form= PostForm(request.POST)
    if request.method=="POST":
        form= PostForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            titulo= informacion["titulo"]
            slug= informacion["slug"]
            intro= informacion["intro"]
            cuerpo= informacion["cuerpo"]
            post = Post(titulo=titulo, slug=slug, intro=intro, cuerpo=cuerpo)
            post.save()
            return render(request, "AppPagina/inicio.html", {"mensaje": "Blog guardado correctamente!"})
        else:
            return render(request, "AppPagina/inicio.html", {"mensaje": "Informacion NO valida"})
    else:
        form: Post()
        return render(request, "AppPagina/inicio.html", {"form": form})
