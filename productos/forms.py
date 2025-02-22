from django import forms
from .models import Producto

class productoForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese aquí el nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese el precio del producto'
                }
            )
        }
        
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio',
            'imagen': 'URL de la imagen',
        }
        
        error_messages = {
            'precio': {'required': 'Este campo es requerido'},
        }
