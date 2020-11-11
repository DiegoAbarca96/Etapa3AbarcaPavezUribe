from django.db import models

# Create your models here.
class Categoria(models.Model):
    modelo = models.CharField(max_length=60)

    def __str__(self):
        return self.modelo

class Televisores(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=15)
    tamanio = models.CharField(max_length=15)
    resolucion = models.CharField(max_length=40)
    smarttv = models.BooleanField()
    tasarefresco = models.CharField(max_length=15)
    usb = models.CharField(max_length=15)
    hdmi = models.CharField(max_length=15)
    imagena = models.ImageField(upload_to="especificaciones", null=True)
    imagenb = models.ImageField(upload_to="especificaciones", null=True)
    imagenc = models.ImageField(upload_to="especificaciones", null=True)

    def __str__(self):
        return self.nombre
        
class Especificaciones(models.Model):
    nombre = models.CharField(max_length=60)
    procesador = models.CharField(max_length=30)
    velocidadProc = models.CharField(max_length=30)
    cantNucleo = models.CharField(max_length=30)
    ram = models.CharField(max_length=30)
    expandibleRAM = models.CharField(max_length=30)
    almacenamiento =models.CharField(max_length=30)
    pantalla = models.CharField(max_length=30)
    resolucion = models.CharField(max_length=30)
    tarjetaVideo = models.CharField(max_length=30)
    modeloTarjeta = models.CharField(max_length=30)
    usb = models.CharField(max_length=30)
    hdmi = models.CharField(max_length=30)
    sistOperativo = models.CharField(max_length=30)
    bateria = models.CharField(max_length=50)
    recomendacion = models.TextField()
    imagena = models.ImageField(upload_to="especificaciones", null=True)
    imagenb = models.ImageField(upload_to="especificaciones", null=True)
    imagenc = models.ImageField(upload_to="especificaciones", null=True)

    def __str__(self):
        return self.nombre