from django import forms
from .models import Categoria

class categoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese aquí el nombre del producto'
                }
            ),
            
        }
        
        labels = {
            'nombre': 'Nombre del producto',
            'imagen': 'URL de la imagen',
        }
