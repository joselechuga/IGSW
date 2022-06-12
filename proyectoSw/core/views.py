from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def log(request):
    return render(request,'core/login.html')

def mousepad(request):
    return render(request,'core/mousepad.html')

def com_tec(request):
    return render(request,'core/combo_teclado.html')