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

class MensajeForm(forms.ModelForm):
    emisor = models.ForeignKey(User, related_name="emisor", on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name="receptor", on_delete=models.CASCADE) 
    cuerpo = forms.TextInput()
    date_added = forms.DateTimeField()
