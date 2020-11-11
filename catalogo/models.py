from django.db import models

# Create your models here.
class Categoria(models.Model):
    modelo = models.CharField(max_length=60)

    def __str__(self):
        return self.modelo

class Especificaciones(models.Model):
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

    def __str__(self):
        return self.procesador