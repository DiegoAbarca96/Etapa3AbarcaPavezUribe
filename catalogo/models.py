from django.db import models

# Create your models here.
class Categoria(models.Model):
    modelo = models.CharField(max_length=60)

    def __str__(self):
        return self.modelo

class Celulares(models.Model):
    nombre = models.CharField(max_length=60)
    tipopantalla = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    ram = models.CharField(max_length=30)
    memoriainterna = models.CharField(max_length=30)
    sistemaoperativo = models.CharField(max_length=30)
    camaraprincipal = models.CharField(max_length=30)
    camarafrontal = models.CharField(max_length=30)
    imagena = models.ImageField(upload_to="celulares", null=True)
    imagenb = models.ImageField(upload_to="celulares", null=True)
    imagenc = models.ImageField(upload_to="celulares", null=True)

    def __str__(self):
        return self.nombre

class Televisores(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=15)
    tamanio = models.CharField(max_length=15)
    resolucion = models.CharField(max_length=40)
    smarttv = models.BooleanField()
    tasarefresco = models.CharField(max_length=15)
    usb = models.CharField(max_length=15)
    hdmi = models.CharField(max_length=15)
    imagena = models.ImageField(upload_to="televisores", null=True)
    imagenb = models.ImageField(upload_to="televisores", null=True)
    imagenc = models.ImageField(upload_to="televisores", null=True)

    def __str__(self):
        return self.nombre
        
class Notebooks(models.Model):
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
    imagena = models.ImageField(upload_to="notebooks", null=True)
    imagenb = models.ImageField(upload_to="notebooks", null=True)
    imagenc = models.ImageField(upload_to="notebooks", null=True)

    def __str__(self):
        return self.nombre