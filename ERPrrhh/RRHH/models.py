from django.db import models

# Create your models here.
class Area(models.Model):
    "Esta es una clase que representa un área" 
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=50)
    descripcion_area = models.TextField(max_length=100)
    encargado = models.OneToOneField('Empleado', blank=True, null=True, on_delete=models.SET_NULL, related_name='area_encargada')

    def __str__(self):
        return str(self.nombre_area) 

class Cargo(models.Model):
    "Esta es una clase que representa un cargo dentro de un área" 
    id_cargo = models.AutoField(primary_key=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='cargos')
    nombre_cargo = models.CharField(max_length=50)
    descripcion_cargo = models.TextField(max_length=100)

    def __str__(self):
        return str(self.nombre_cargo)

class Empleado(models.Model):
    "Esta es una clase que representa un empleado"
    carnet = models.CharField(max_length=6, primary_key=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='empleados')
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dui = models.CharField(max_length=9)
    sexo = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
        ]
    roles = [
        ('1', 'Administrador'),
        ('2', 'Empleado')
        ]
    rol = models.CharField(max_length=1, choices=roles, default='2')
    genero = models.CharField(max_length=1, choices=sexo, default='M')
    fechanacimiento = models.DateField()
    direccion = models.TextField()
    salariobase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombres} {self.apellidos} {self.rol}'

class Usuario(models.Model):
    "Esta es una clase que representa un usuario del sistema"
    id_usuario = models.AutoField(primary_key=True)
    carnet = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='usuarios')
    password = models.TextField(max_length=256)

    def __str__(self):
        return str(self.carnet)

class Departamento(models.Model):
    "Esta es una clase que representa un departamento del pais El Salvador"
    id_departamento = models.AutoField(primary_key=True)
    carnet = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='departamentos', blank=True, null=True)
    nombre_departamento = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre_departamento)

class Municipio(models.Model):
    "Esta es una clase que representa un municipio del pais El Salvador" 
    id_municipio = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='municipios')
    nombre_municipio = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre_municipio)

class Pago(models.Model):
    "Esta es una clase que representa un pago"
    codigo_pago = models.AutoField(primary_key=True)
    carnet = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='pagos')
    bono = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    totalpagar = models.DecimalField(max_digits=10, decimal_places=2)
    isss = models.DecimalField(max_digits=10, decimal_places=2)
    afp = models.DecimalField(max_digits=10, decimal_places=2)
    renta = models.DecimalField(max_digits=10, decimal_places=2)
    fechapago = models.TimeField()

    def __str__(self):
        return f'Pago {self.codigo_pago} - {self.carnet}'

class Asistencia(models.Model):
    "Esta es una clase que representa la asistencia de un empleado"
    id_asistencia = models.AutoField(primary_key=True)
    carnet = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='asistencias')
    horas_trabajadas = models.IntegerField(default=0)
    horas_extras_diurnas = models.IntegerField(default=0)
    horas_extras_nocturnas = models.IntegerField(default=0) 
    mes = [
        ('1', 'Enero'),
        ('2', 'Febrero'),
        ('3', 'Marzo'),
        ('4', 'Abril'),
        ('5', 'Mayo'),
        ('6', 'Junio'),
        ('7', 'Julio'),
        ('8', 'Agosto'),
        ('9', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
        ]
    mes_asistencia = models.CharField(max_length=2, choices=mes, default='1')

    def __str__(self):
        return f'Asistencia {self.id_asistencia} - {self.carnet}'

class Permiso(models.Model):
    "Esta es una clase que representa un permiso de un empleado"
    codigo_permiso = models.AutoField(primary_key=True)
    carnet = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='permisos')
    fechainicio = models.DateField()
    fechafinal = models.DateField()
    justificacion = models.TextField()
    estado = [
        ('1', 'Aprobado'),
        ('2', 'Rechazado'),
        ('3', 'Pendiente'),
        ]
    estado = models.CharField(max_length=10, choices=estado, default='Pendiente')

    def __str__(self):
        return f'Permiso {self.codigo_permiso} - {self.carnet}'