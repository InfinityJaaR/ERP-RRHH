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

def GestionarEmpleadosView(request, id="RM0009"):
    empleado = get_object_or_404(Empleado, carnet=id)
    return render(request, 'EMgestionarEmpleado.html', {'empleado': empleado})

def AdministrarCargoView(request):
    cargos=Cargo.objects.all()
    data={
        'cargos': cargos
    }
    return render(request, "ADadministrarCargo.html", data)

def GestionarPermisosView(request, id="RM0009"):
    empleado = get_object_or_404(Empleado, carnet=id) 

    permisos = Permiso.objects.filter(carnet=empleado)
    
    return render(request, 'EMgestionarPermisos.html', {'permisos': permisos, 'empleado':empleado})

def SolicitarPermisoView(request, id="RM0009"):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, carnet=id)
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        razon = request.POST.get('razon')

        # Crear una nueva instancia de Permiso
        permiso = Permiso(
            #carnet=request.user.empleado,  # Asocia el permiso al empleado logueado
            carnet=empleado,
            fechainicio=fecha_inicio,
            fechafinal=fecha_fin,
            justificacion=razon,
            estado = '3'# Estado inicial del permiso
            #fecha_solicitud=timezone.now()  # Fecha en la que se solicita el permiso
        )
        permiso.save()

        return redirect('gestionar_permisosEM')  # Redirige a la página de gestión de permisos
    return render(request, 'EMsolicitarPermiso.html')

def GestionarPagoEMView(request, id="RM0009"):
    empleado = get_object_or_404(Empleado, carnet=id)
    fecha_pago = request.GET.get('fechaPago')
    if fecha_pago:
        pagos = Pago.objects.filter(carnet=empleado, fechapago=fecha_pago)
    else:
        pagos = Pago.objects.filter(carnet=empleado)
    return render(request, 'EMgestionarPago.html', {'pagos': pagos, 'empleado': empleado})


def CrearPagoView(request):
    return render(request, "ADcrearPagos.html")

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