from django.shortcuts import render, redirect
from .models import Sucursales
# Create your views here.

def inicio_vista(request):
    lassucursales=Sucursales.objects.all()
    return render(request,"gestionarSucursales.html", {"missucursales":lassucursales}   )

def registrarSucursales(request):
    idSucursales=request.POST["txtidSucursales"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    ciudad=request.POST["txtciudad"]
    gerente=request.POST["txtgerente"]
    horarioAtencion=request.POST["txthorarioAtencion"]

    guardarSucursales=Sucursales.objects.create(
    idSucursales=idSucursales, nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad, gerente=gerente, horarioAtencion=horarioAtencion
    ) #GUARDA EL REGISTRO

    return redirect("/")

def seleccionarSucursales(request, idSucursales):
    sucursal=Sucursales.objects.get(idSucursales=idSucursales)
    return render(request,"editarSucursales.html",{"missucursales":sucursal})

def editarSucursales(request):
    idSucursales=request.POST["txtidSucursales"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    ciudad=request.POST["txtciudad"]
    gerente=request.POST["txtgerente"]
    horarioAtencion=request.POST["txthorarioAtencion"]
    sucursal=Sucursales.objects.get(idSucursales=idSucursales)
    sucursal.nombre=nombre
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    sucursal.ciudad=ciudad
    sucursal.gerente=gerente
    sucursal.horarioAtencion=horarioAtencion
    sucursal.save() # guardar registro actualizado
    return redirect("/")

def borrarSucursales(request, idSucursales):
    sucursal=Sucursales.objects.get(idSucursales=idSucursales)
    sucursal.delete() # borrar el registro
    return redirect("/")