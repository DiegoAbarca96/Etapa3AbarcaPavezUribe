from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contenido/acer', views.acer, name='acer'),
    path('contenido/lenovo', views.lenovo, name='lenovo'),
    path('contenido/asus', views.asus, name='asus'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('producto', views.producto, name='producto'),
]