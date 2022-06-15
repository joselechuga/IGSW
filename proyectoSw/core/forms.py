from django import forms
from django.forms import ModelForm
from .models import nuevoUsuario

class nuevoUsuarioForm(ModelForm):
    class Meta:
        model = nuevoUsuario
        fields = ['nombreUsuario','psw','email','edad','genero']