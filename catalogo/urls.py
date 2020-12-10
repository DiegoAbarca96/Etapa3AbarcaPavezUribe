from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('agregar-producto', views.agregar_producto, name='agregar_producto'),
    path('listar-productos', views.listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('contacto', views.contacto, name='contacto'),
    path('eliminar-usuario/<id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('listar-usuarios', views.listar_usuarios, name='listar_usuarios'),
    path('modificar-usuario/<id>/', views.modificar_usuario, name='modificar_usuario'),
    
]