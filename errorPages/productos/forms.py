#Define los formularios de los modelos en esta App

from django import forms
from .models import Producto

#Se debe crear una clase para cada modelo

class productoForm(forms.ModelForm):
    #Meta es la clase que define la meta-informacion del formulario
    class Meta:
        #De que modelo se basa este formulario
        model = Producto

        #Que campos se van a ver en el formulario
        fields = ['nombre', 'precio','imagen','categoria']

        #Personalizar la apariencia del formulario(widgets)

        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Nombre delk producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Imagen del producto'
                }
            ),
            'cartegoria':forms.Select(
                attrs={
                    'class':'form-input'
                }
            )
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen',
            'categoria':'Categoria del producto'
        }

        #Mensajes de error
        error_messages = {
            'nombre':{
                'required': 'El nombre es requerido'
            },
            'precio':{
                'required': 'El  precio no puede estar vacío',
                'invalid': 'Ingresa un número válido'

            }
        }