from django.db import models

# Create your models here.
class Sucursales(models.Model):
    idSucursales=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=30)
    gerente=models.CharField(max_length=50)
    horarioAtencion=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre