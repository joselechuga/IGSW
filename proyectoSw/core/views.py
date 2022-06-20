from contextvars import Context
from multiprocessing import context
from telnetlib import AUTHENTICATION
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import nuevoUsuarioForm

#from core.models import nuevoUsuario
from .models import nuevoUsuario
# Create your views here.

def index(request):
    return render(request,'core/index.html')

def log(request):
    return render(request,'core/login.html')

def mousepad(request):
    return render(request,'core/mousepad.html')

def com_tec(request):
    return render(request,'core/combo_teclado.html')

def form_registrousu(request):
    datos={
        'form': nuevoUsuarioForm()


    }
    if request.method == 'POST':
        formulario = nuevoUsuarioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'El usuario se ha registrado correctamente'

    return render(request,'core/form_registrousu.html',datos)

def login(request):
    if request.method=='POST':
        try:
            detalleUsuario= nuevoUsuario.objects.get(Email=request.POST['email'], psw=request.POST['password'])
            print("Usuario",detalleUsuario)
            request.session['Email']=detalleUsuario.Email
            return render(request,'core/index.html')
        except nuevoUsuario.DoesNotExist as e:
            messages.error(request,'Usuario o contraseña incorrectos')
    return render(request, 'login.html')
