from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.

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

def agregar_producto(request):
    
    data = {
        'form': ProductoForm()
    }

    if  request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente!"
        else:
            data["form"] = formulario
    return render(request, 'app/crud/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }


    return render(request, 'app/crud/listar.html', data)