from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Modelo de Usuario Personalizado
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
    )
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_doc = models.CharField(max_length=20, choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería')])
    num_doc = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(unique=True)
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, default='empleado')

    def __str__(self):
        return f"{self.nombre} ({self.get_user_type_display()})"

    def puede_registrar_empleados(self):
        return self.user_type == 'administrador'

    def puede_registrar_propietarios_y_vehiculos(self):
        return self.user_type in ['administrador', 'empleado']

<<<<<<< HEAD
from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_doc = models.CharField(max_length=20, choices=[
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería')
    ])
    num_doc = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.num_doc}"


=======
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
# Modelo de Vehículo
class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=10, unique=True)
<<<<<<< HEAD
    tipo_vehiculo = models.CharField(max_length=50, choices=[
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
        ('Bicicleta', 'Bicicleta')
    ])
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='vehiculos')
    estado = models.BooleanField(default=False)  # False = "afuera", True = "adentro"

    def save(self, *args, **kwargs):
        self.placa = self.placa.upper()
        super().save(*args, **kwargs)

=======
    tipo_vehiculo = models.CharField(max_length=50, choices=[('Carro', 'Carro'), ('Moto', 'Moto'), ('Bicicleta', 'Bicicleta')])
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    propietario = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=False)  # False = "afuera", True = "adentro"

>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
    def __str__(self):
        return f"{self.placa} - {self.tipo_vehiculo} ({self.marca}, {self.color})"

# Modelo de Celda
class Celda(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Celda {self.numero} - {'Disponible' if self.disponible else 'Ocupada'}"

# Modelo de Registro de Asignación ( Vehículo)
class RegistroAsignacion(models.Model):
    empleado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='asignaciones', limit_choices_to={'user_type': 'empleado'})
<<<<<<< HEAD
=======
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='clientes', limit_choices_to={'user_type': 'cliente'})
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    celda = models.OneToOneField(Celda, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
    def save(self, *args, **kwargs):
        if not self.celda.disponible:
            raise ValueError(f"La celda {self.celda.numero} ya está ocupada.")
        super().save(*args, **kwargs)
        self.celda.disponible = False
        self.celda.save()

    def __str__(self):
        return f"Asignación: {self.vehiculo.propietario.nombre} - Vehículo: {self.vehiculo.placa} - Celda: {self.celda.numero}"
=======
    def __str__(self):
        return f"Asignación: {self.usuario.nombre} - Vehículo: {self.vehiculo.placa} - Celda: {self.celda.numero}"
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4

# Modelo de Registro de Ingreso y Salida
class RegistroVehiculo(models.Model):
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')], default= 'salida')  # Campo tipo
    fecha_hora_ingreso = models.DateTimeField(blank=True, null=True)
    fecha_hora_salida = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehiculo.placa} - {self.tipo}"
