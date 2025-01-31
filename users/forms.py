from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

#primer formulario
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-input',
                'pattern': '^$',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'required': True
            }
        )
    )


    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']
        #Si quiero editar la forma de los inputs necesito widgets
        widgets = {
            #Cada uno de los widgets del MODELO
            'email': forms.EmailInput(
                #Características de elemento visual
                attrs = {
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes ingresar un correo válido de la utez'
                }
            )
        }


#segundo formulario (inicio de sesion)
class CustomUserLoginForm(AuthenticationForm):
    pass
