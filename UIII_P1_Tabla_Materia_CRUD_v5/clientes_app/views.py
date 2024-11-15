from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarCliente.html", {"misclientes":losclientes}   )

def registrarClientes(request):
    idCliente=request.POST["txtidCliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    fechaRegistro=request.POST["txtfechaRegistro"]

    guardarcliente=Cliente.objects.create(
    idCliente=idCliente, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, correo=correo, fechaRegistro=fechaRegistro
    ) #GUARDA EL REGISTRO

    return redirect("/")

def seleccionarClientes(request, idCliente):
    cliente=Cliente.objects.get(idCliente=idCliente)
    return render(request,"editarcliente.html",{"misclientes":cliente})

def editarClientes(request):
    idCliente=request.POST["txtidCliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    fechaRegistro=request.POST["txtfechaRegistro"]
    cliente=Cliente.objects.get(idCliente=idCliente)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.direccion=direccion
    cliente.telefono=telefono
    cliente.correo=correo
    cliente.fechaRegistro=fechaRegistro
    cliente.save() # guardar registro actualizado
    return redirect("/")

def borrarClientes(request, idCliente):
    cliente=Cliente.objects.get(idCliente=idCliente)
    cliente.delete() # borrar el registro
    return redirect("/")