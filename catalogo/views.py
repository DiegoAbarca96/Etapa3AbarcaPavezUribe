from django.shortcuts import render

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