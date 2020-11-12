from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm, ContactoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    productos = Producto.objects.all()

    context = {'productos':productos}

    return render(request,'app/homea.html', context)

def registro(request):
    
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="login")
    return render(request,'app/registro.html', data)

def agregar_producto(request):
    
    data = {
        'form': ProductoForm()
    }

    if  request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
        else:
            data["form"] = formulario
    return render(request, 'app/crud/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    context = {'productos':productos}


    return render(request, 'app/crud/listar.html', context)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if  request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'app/crud/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Envio exitoso"
        else:
            data["form"] = formulario 

    return render(request, "app/contacto.html", data)