from django import forms

class UsuarioForm(forms.Form):
    name=forms.CharField(label="name", max_length=20)
    email=forms.EmailField(label="email", max_length=30)
    password=forms.CharField(label="password", max_length=30)
