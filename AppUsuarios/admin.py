from django.contrib import admin
from .models import *
from AppPagina.models import Post

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Avatar)


