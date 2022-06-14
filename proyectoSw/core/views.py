from django.shortcuts import render
from django.contrib import messages
from core.models import nuevoUsuario
# Create your views here.

def index(request):
    return render(request,'core/index.html')

def log(request):
    return render(request,'core/login.html')

def mousepad(request):
    return render(request,'core/mousepad.html')

def com_tec(request):
    return render(request,'core/combo_teclado.html')

def registroUsuario(request):
    if request.method== 'POST':
        nombreUsuario=request.POST.get('nombreUsuario')
        psw=request.POST.get('password')
        email=request.POST.get('correo')
        edad=request.POST.get('edad')
        genero=request.POST.get('genero')
        nuevoUsuario(nombreUsuario=nombreUsuario,psw=psw,email=email,edad=edad,genero=genero).save()
        messages.success(request,'el usuario'+request.POST['nombreUsuario']+'se ha registrado correctamente')
        return render(request,'core/registrarse.html')
    else:
        return render(request,'core/registrarse.html')
