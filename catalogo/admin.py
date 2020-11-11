from django.contrib import admin
from .models import Categoria, Notebooks, Televisores, Celulares
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Notebooks)
admin.site.register(Televisores)
admin.site.register(Celulares)