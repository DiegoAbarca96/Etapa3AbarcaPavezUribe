from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="celulares", null=True)

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
