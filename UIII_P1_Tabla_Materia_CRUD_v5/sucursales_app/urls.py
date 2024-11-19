from django.urls import path
from sucursales_app import views
urlpatterns = [
    path("", views.inicio_vista, name= "inicio_vista" ),
    path("registrarSucursales/",views.registrarSucursales,name="registrarSucursales"),
    path("seleccionarSucursales/<codigo>",views.seleccionarSucursales,name="seleccionarSucursales"),
    path("editarSucursales/",views.editarSucursales,name="editarSucursales"),
    path("borrarSucursales/<codigo>", views.borrarSucursales,name="borrarSucursales"),
    
]
