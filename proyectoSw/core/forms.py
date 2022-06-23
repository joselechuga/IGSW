from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import nuevoUsuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class nuevoUsuarioForm(ModelForm):
    class Meta:
        model = nuevoUsuario
        fields = ['nombreUsuario','psw','email','edad','genero']

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }



    