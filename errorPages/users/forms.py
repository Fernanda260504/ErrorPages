from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Primer formulario - Registro de usuario
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'pattern': r'^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Necesitas definir una contraseña segura:\n'
                         '- Al menos un número.\n'
                         '- Al menos una letra mayúscula.\n'
                         '- Al menos un carácter especial (!#$%&?).\n'
                         '- Mínimo de 8 caracteres en total.',
                'required': True
            }
        )
    )

    password2 = forms.CharField(
        label='Repite tu Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'pattern': r'^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Repita su contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'required': True
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        # Definiendo widgets personalizados para cada campo
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes ingresar un correo electrónico válido de la UTEZ'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': r'^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$',
                    'title': 'Necesitas ingresar una matrícula válida de la UTEZ',
                    'maxlength': '20'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': r'^[0-9]+$',
                    'title': 'Ingrese solo números',
                    'max': '100',
                    'min': '1'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': r'^[0-9\+-]{10}$',
                    'title': 'Ingrese solo números',
                    'maxlength': '15'
                }
            )
        }

# Segundo formulario - Inicio de sesión
class CustomUserLoginForm(AuthenticationForm):
    pass
