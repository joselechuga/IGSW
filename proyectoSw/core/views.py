from contextvars import Context
from email import message
from multiprocessing import context
from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import nuevoUsuarioForm, UserRegisterForm
from .models import *
from django.contrib import messages

#from core.models import nuevoUsuario
from .models import nuevoUsuario
# Create your views here.

def index(request):
    return render(request,'core/index.html')

def log(request):
    return render(request,'core/logins/login.html')

def mousepad(request):
    return render(request,'core/mousepad.html')

def com_tec(request):
    return render(request,'core/combo_teclado.html')

def selpago(request):
    return render(request,'core/pagos/selpago.html')

def confirmapago(request):
    return render(request,'core/pagos/confirmapago.html')
def carrito(request):
    return render(request,'core/productos/carrito.html')
def combored (request):
    return render(request,'core/productos/combored.html')

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form=UserRegisterForm()
    
    context = { 'form' : form}
    return render(request,'core/logins/register.html', context) 