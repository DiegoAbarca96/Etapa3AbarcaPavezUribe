from django.shortcuts import render
from .models import Notebooks, Televisores, Celulares

# Create your views here.

def producto(request):
    cel_info=Celulares.objects.all()
    note_info=Televisores.objects.all()
    tel_info=Notebooks.objects.all()

    cel_info={'cel_info':cel_info},
    note_info={'note_info':note_info},
    tel_info={'tel_info':tel_info}
    
    return render(
        request,
        'app/contenido/producto.html',
        cel_info,
        note_info,
        tel_info
        
    )

def home(request):

    return render(
        request,
        'app/home.html'
    )

def acer(request):
    
    return render(
        request,
        'app/contenido/pc1.html'
    )

def lenovo(request):
    
    return render(
        request,
        'app/contenido/pc2.html'
    )

def asus(request):
    
    return render(
        request,
        'app/contenido/pc3.html'
    )

def login(request):
    
    return render(
        request,
        'app/login.html'
    )

def registro(request):
    
    return render(
        request,
        'app/registro.html'
    )