#Define los formularios de los modelos en esta App

from django import forms
from .models import Alumno

#Se debe crear una clase para cada modelo

class alumnoForm(forms.ModelForm):
    #Meta es la clase que define la meta-informacion del formulario
    class Meta:
        #De que modelo se basa este formulario
        model = Alumno

        #Que campos se van a ver en el formulario
        fields = ['id', 'nombre','apellidos','edad','matricula','correo',]

        #Personalizar la apariencia del formulario(widgets)

        widgets = {
            'id': forms.NumberInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Id del Alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre del alumno'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Edad del alumno'
                }
            ),
              'matricula': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Matricula del alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Correo del alumno'
                }
            ),

        }

        #Personalizar las etiquetas
        labels = {
            'id':'Id del alumno',
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad':'Edad del alumno',
            'matricula': 'Matricula del alumno',
            'correo':'Correo del alumno'
        }

        #Mensajes de error
        error_messages = {
             'id':{
                'required': 'El id es requerido'
            },
            'nombre':{
                'required': 'El nombre es requerido'
            },
            'apellido':{
                'required': 'El apellido es requerido'
            },
             'edad':{
                'required': 'La edad es requerido'
            },

            'matricula':{
                'required': 'La matricula es requerida'
            },
             'correo':{
                'required': 'El correo es requerido'
            },
        }