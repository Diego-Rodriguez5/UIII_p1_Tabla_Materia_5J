from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=50)
    fechaRegistro=models.DateField()

    def __str__(self):
        return self.nombre