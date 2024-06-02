# urls.py en tu aplicación
from django.urls import path
from .views import *

urlpatterns = [
   
    path('empleado/perfil', GestionarEmpleadosView, name="perfil_empleado"),
    path('empleado/permisos',GestionarPermisosView, name='gestionar_permisosEM'),
    path('administrador/organizacion/cargos', AdministrarCargoView, name="AdministrarCargoView"),
    path('administrador/pagos/nuevoPago',CrearPagoView),
    path('empleado/permisos/solicitarPermiso',SolicitarPermisoView, name='solicitar_permiso'),
    path('',HomeView, name= "HomeView"),
    #ruta pantallas Eduardo
    path('administrador/Organizacion/areas',AdministrarAreaView, name="AdministrarAreaView"),
    path('administrador/Organizacion/areas/gestionarArea',GestionarAreaView),
    path('administrador/Organizacion/cargos/gestionarCargo',GestionarCargoView, name="GestionarCargoView"),
    path('administrador/permisos',GestionarPermisoADView),
    path('administrador/Organizacion',GestionarOrganizacionView,name="GestionarOrganizacionView"),
    path('administrador/pagos/modificar',ModificarPagoView),
    path('administrador/empleado',GestionarEmpleadoADView),
    path('administrador/asistencia',RegistrarAsistenciaView),
    path('administrador/pagos',GestionarPagoADView),
    path('empleado/pagos',GestionarPagoEMView, name='mis_pagos'),
    path('EliminarCargo/<int:id>', EliminarCargo, name="EliminarCargo"),
    path('EliminarArea/<int:id>', EliminarArea, name="EliminarArea"),
    path('EliminarEmpleadp/<id>', EliminarEmpleado, name="EliminarEmpleado"),
    path('ModificarCargo/<id>', ModificarCargo, name="ModificarCargo"),
    path('ModificarArea/<id>', ModificarArea, name="ModificarArea"),
]
