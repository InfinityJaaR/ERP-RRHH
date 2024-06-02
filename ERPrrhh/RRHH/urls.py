# urls.py en tu aplicación
from django.urls import path
from .views import *

urlpatterns = [
   
    path('empleado/perfil', GestionarEmpleadosView),
    path('empleado/permisos',GestionarPermisosView),
    path('administrador/organizacion/cargos', AdministrarCargoView, name="AdministrarCargoView"),
    path('administrador/pagos/nuevoPago',CrearPagoView),
    path('administrador/permisos/solicitarPermiso',SolicitarPermisoView),
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
    path('empleado/pagos',GestiionarPagoEMView),
    path('EliminarCargo/<int:id>', EliminarCargo, name="EliminarCargo"),
    path('EliminarArea/<int:id>', EliminarArea, name="EliminarArea"),
    path('EliminarEmpleadp/<id>', EliminarEmpleado, name="EliminarEmpleado"),
    path('ModificarCargo/<id>', ModificarCargo, name="ModificarCargo"),
    path('ModificarArea/<id>', ModificarArea, name="ModificarArea"),
]
