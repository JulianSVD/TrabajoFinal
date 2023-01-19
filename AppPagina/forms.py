from django import forms
from .models import *


class PostForm(forms.ModelForm):
    titulo = forms.TextInput()
    slug = forms.SlugField()
    intro =  forms.TextInput()
    cuerpo = forms.Textarea()
    date_added = forms.DateTimeField()
    image= models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
