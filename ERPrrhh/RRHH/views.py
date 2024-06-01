from django.shortcuts import render, redirect, get_object_or_404
from .models import Area, Cargo, Empleado, Usuario, Departamento, Municipio, Pago, Asistencia, Permiso
from .froms import CargoForm, AreaForm

# Create your views here.
def GestionarEmpleadosView(request):
    return render(request, 'EMgestionarEmpleado.html')

def AdministrarCargoView(request):
    cargos=Cargo.objects.all()
    data={
        'cargos': cargos
    }
    return render(request, "ADadministrarCargo.html", data)

def CrearPagoView(request):
    return render(request, "ADcrearPagos.html")

def SolicitarPermisoView(request):
    return render(request, "ADsolicitarPermiso.html")

def GestionarPermisosView(request):
    return render(request, "EMgestionarPermisos.html")

def HomeView(request):
    return render(request, "inicio.html")

#Pantallas de Eduardo
def LoginView(request):
    return render(request, "login.html")

def AdministrarAreaView(request):
    areas=Area.objects.all()
    data={
        'areas':areas
    }
    return render(request, "ADadministrarArea.html", data)

def GestionarAreaView(request):
    data={
        'form': AreaForm()
    }
    if request.method == 'POST':
        formulaio= AreaForm(data=request.POST)
        if formulaio.is_valid():
            formulaio.save()
            data["mensaje"]= "Guardado correctamente"
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarArea.html", data)

def GestionarCargoView(request):
    data={
        'form': CargoForm()
    }
    if request.method == 'POST':
        formulaio= CargoForm(data=request.POST)
        if formulaio.is_valid():
            formulaio.save()
            data["mensaje"]= "Guardado correctamente"
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarCargo.html", data)

def GestionarPermisoADView(request):
    return render(request, "ADgestionarPermiso.html")

def GestionarOrganizacionView(request):
    empleados=Empleado.objects.all()
    data = {
        'empleados': empleados

    }
    return render(request, "ADgestionarOrganizacion.html", data)

def ModificarPagoView(request):
    return render(request, "ADmodificarPago.html")

def GestionarEmpleadoADView(request):
    return render(request, "ADgestionarEmpleado.html")

def RegistrarAsistenciaView(request):
    return render(request, "ADregistrarAsistencia.html")

def GestionarPagoADView(request):
    return render(request, "ADgestionarPago.html")

def GestiionarPagoEMView(request):
    return render(request, "EMgestionarPago.html")

def EliminarCargo(request, id):
    cargo = get_object_or_404(Cargo, id_cargo=id)
    cargo.delete()
    return redirect("AdministrarCargoView")

def EliminarArea(request, id):
    cargo = get_object_or_404(Area, id_area=id)
    cargo.delete()
    return redirect("AdministrarAreaView")

def EliminarEmpleado(request, id):
    cargo = get_object_or_404(Empleado, carnet=id)
    cargo.delete()
    return redirect("GestionarOrganizacionView")

def ModificarCargo(request, id):
    cargo= get_object_or_404(Cargo, id_cargo=id)
    data={
        'form':CargoForm(instance=cargo)
    }
    if request.method == 'POST':
        formulaio= CargoForm(data=request.POST, instance=cargo)
        if formulaio.is_valid():
            formulaio.save()
            return redirect("AdministrarCargoView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarCargo.html", data)

def ModificarArea(request, id):
    area= get_object_or_404(Area, id_area=id)
    data={
        'form':AreaForm(instance=area)
    }
    if request.method == 'POST':
        formulaio= AreaForm(data=request.POST, instance=area)
        if formulaio.is_valid():
            formulaio.save()
            return redirect("AdministrarAreaView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarArea.html", data)