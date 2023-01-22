from django.shortcuts import render
from AppPagina.models import *
from AppUsuarios.models import *
from AppUsuarios.views import *
from AppPagina.forms import PostForm, MensajeForm

def inicio(request):
    return render (request, "AppPagina/inicio.html", {"avatar": obtenerAvatar(request)})
    
def blogs(request):
    posts = Post.objects.all()    
    return render(request, "AppPagina/blogs.html", {"posteos": posts, "avatar": obtenerAvatar(request)})


def leer_mas(request, slug):
 posts = Post.objects.get(slug=slug)
 return render(request, "AppPagina/leer_mas.html", {"posteos": posts})

def eliminarBlog(request, id):
    blog=Post.objects.get(id=id)
    blog.delete()
    posts=Post.objects.all()
    return render(request, "AppPagina/inicio.html", {"posteos": posts})

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

#__________________MENSAJERIA__________________________#

# def index(request): Creo que es para todo el sitio
#     mensajes = Mensaje.objects.all()
#     return render (request, 'index.html', {'mensajes' : mensajes, 'form' : MensajeForm()})

def buzon(request):
        mensajes = Mensaje.objects.all()#To_user = request.user.username)
        return render(request, 'AppPagina/buzon.html', {'mensajes': mensajes})

# PARA ENVIAR MENSAJE!
def enviarMensaje(request):
    form= MensajeForm(request.POST)
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            emisor=informacion["emisor"]
            receptor=informacion["receptor"]
            cuerpo=informacion["cuerpo"]
            post = Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo)
            post.save()
            return render(request, "AppPagina/inicio.html", {"mensaje": "Mensaje enviado correctamente!"})
        else:
            return render(request, "AppPagina/inicio.html", {"mensaje": "Error al enviar mensaje"})
    else:
        form: Post()
        return render(request, "AppPagina/inicio.html", {"form": form})

# def blogs(request):
#     posts = Post.objects.all()    
#     return render(request, "AppPagina/blogs.html", {"posteos": posts, "avatar": obtenerAvatar(request)})
