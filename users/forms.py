from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate
import re

#primer formulario
class CustomUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                # 'pattern': '^$',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'required': True
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña 2',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                # 'pattern': '^$',
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
                attrs={
                'class': 'form-control',
                'required': True,
                'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
                'title': 'Debes ingresar un correo válido de la UTEZ',
                'placeholder': 'Debes ingresar un email'
            }),
            'name': forms.TextInput(
                attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Ingrese su nombre'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Ingrese su apellido'
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'pattern': '^[0-9]{5}[a-z]{2}[0-9]{3}',
                'maxlength': 20,
                'placeholder': 'Necesitas agregar una matricula de la UTEZ'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'pattern': '^[0-9]+$',
                'min_value': 5,
                'placeholder': 'Ingrese solo números',
                'max_value': 100
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': r'^[0-9\+-]{10}',
                'required': True,
                'minlength': 10,
                'maxlength': 10,
                'placeholder': 'Ingrese su teléfono'
            }),
            
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9]+@utez\.edu\.mx$', email):
            raise forms.ValidationError('Debes ingresar un correo válido de la UTEZ.')
        return email
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match(r'^[0-9]{5}[a-z]{2}[0-9]{3}$', control_number):
            raise forms.ValidationError('La matrícula debe seguir el formato: 20223tn089.')
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if len(tel) != 10 or not tel.isdigit():
            raise forms.ValidationError('El teléfono debe tener exactamente 10 dígitos.')
        return tel

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        
        if len(password1) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        if not re.search(r'[0-9]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos un número.')
        
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos una letra mayúscula.')
        
        if not re.search(r'[!#$%&?]', password1):
            raise forms.ValidationError('La contraseña debe contener al menos un carácter especial (!#$%&?).')
        
        return password2

#segundo formulario (inicio de sesion)
class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Correo electrónico",
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
                'title': 'Debes ingresar un correo válido de la UTEZ',
                'placeholder': 'Debes ingresar un email',
            }
        )
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'required': True,
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data
