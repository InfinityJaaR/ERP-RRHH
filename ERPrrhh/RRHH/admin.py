from django.contrib import admin
from .models import Area, Cargo, Empleado, Usuario, Departamento, Municipio, Pago, Asistencia, Permiso

# Register your models here.
admin.site.register(Area)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Pago)
admin.site.register(Asistencia)
admin.site.register(Permiso)