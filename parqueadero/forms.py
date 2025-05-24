from django import forms
<<<<<<< HEAD
from .models import RegistroVehiculo, CustomUser, Vehiculo, Usuario, Celda
=======
from .models import RegistroVehiculo, CustomUser, Vehiculo
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4

class RegistroEntradaForm(forms.ModelForm):
    class Meta:
        model = RegistroVehiculo
        fields = ['vehiculo']

class RegistroSalidaForm(forms.ModelForm):
    class Meta:
        model = RegistroVehiculo
        fields = ['fecha_hora_salida']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'tipo_doc', 'num_doc', 'telefono', 'correo', 'user_type']
        widgets = {
            'user_type': forms.Select(choices=[('empleado', 'Empleado')]),  # Solo permitir empleados
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
<<<<<<< HEAD
        fields = ['placa', 'tipo_vehiculo', 'marca', 'color', 'usuario']
=======
        fields = ['placa', 'tipo_vehiculo', 'marca', 'color', 'propietario']  # Campos existentes en el modelo
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la placa'}),
            'tipo_vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la marca'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el color'}),
<<<<<<< HEAD
            'usuario': forms.Select(attrs={
                'class': 'form-control select2',
                'placeholder': 'Buscar propietario...'
            }),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'tipo_doc', 'num_doc', 'telefono', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre completo'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-control'}),
            'num_doc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de documento'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
        }

class CeldaForm(forms.ModelForm):
    class Meta:
        model = Celda
        fields = ['numero']
        labels = {
            'numero': 'Número de celda'
=======
            'propietario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el propietario'}),
>>>>>>> 8e9dc2bfcace5fa602bd7987f79fbddfa75f53f4
        }

