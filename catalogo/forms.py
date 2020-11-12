from django import forms
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto 
        fields = ["nombre", "email", "tipo_consulta", "mensaje"]

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]