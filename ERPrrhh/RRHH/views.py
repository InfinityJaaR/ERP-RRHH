from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Area, Cargo, Empleado, Departamento, Municipio, Pago, Asistencia, Permiso
from .froms import CargoForm, AreaForm
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q


# Create your views here.

# def index(request):
#     return render(request, "login.html")

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
            return redirect("AdministrarAreaView")
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
            return redirect("AdministrarCargoView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarCargo.html", data)

def GestionarPermisoADView(request):
    return render(request, "ADgestionarPermiso.html")

def GestionarOrganizacionView(request):
    busqueda = request.GET.get("buscar")
    empleados=Empleado.objects.all()
    page= request.GET.get('page', 1)

    if busqueda:
        empleados = Empleado.objects.filter(
            Q(carnet__icontains =busqueda)|
            Q(nombres__icontains = busqueda)|
            Q(apellidos__icontains = busqueda)|
            Q(area__nombre_area__icontains = busqueda)|
            Q(cargo__nombre_cargo__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(empleados, 10)
        empleados= paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': empleados,
        'paginator': paginator
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