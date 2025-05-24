from django.contrib import admin
<<<<<<< HEAD
from .models import CustomUser, Vehiculo, Celda, RegistroAsignacion, RegistroVehiculo, Usuario
=======
from .models import CustomUser, Vehiculo, Celda, RegistroAsignacion, RegistroVehiculo
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id_persona', 'nombre', 'tipo_doc', 'num_doc', 'telefono', 'correo', 'user_type')
    search_fields = ('nombre', 'num_doc', 'correo')
    list_filter = ('user_type',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id_vehiculo', 'placa', 'tipo_vehiculo', 'marca', 'color', 'usuario')
=======
    list_display = ('id_vehiculo', 'placa', 'tipo_vehiculo', 'marca', 'color', 'propietario')
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
    search_fields = ('placa', 'marca', 'color')
    list_filter = ('tipo_vehiculo',)

@admin.register(Celda)
class CeldaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'disponible')
    list_filter = ('disponible',)

@admin.register(RegistroAsignacion)
class RegistroAsignacionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('empleado', 'vehiculo_usuario', 'vehiculo', 'celda', 'fecha_asignacion')

    def vehiculo_usuario(self, obj):
        return obj.vehiculo.usuario
    vehiculo_usuario.short_description = 'Usuario'
=======
    list_display = ('empleado', 'usuario', 'vehiculo', 'celda', 'fecha_asignacion')
    search_fields = ('usuario__nombre', 'vehiculo__placa', 'celda__numero')
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4

@admin.register(RegistroVehiculo)
class RegistroVehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha_hora_ingreso', 'fecha_hora_salida')
    search_fields = ('vehiculo__placa',)  # Cambia a una tupla (nota la coma al final)
    list_filter = ('fecha_hora_ingreso', 'fecha_hora_salida')
<<<<<<< HEAD
    
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_doc', 'num_doc', 'telefono', 'correo')
    search_fields = ('nombre', 'num_doc', 'correo')
    list_filter = ('tipo_doc',)
=======
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
