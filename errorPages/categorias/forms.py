#Define los formularios de los modelos en esta App

from django import forms
from .models import Categoria

#Se debe crear una clase para cada modelo

class categoriasForm(forms.ModelForm):
    #Meta es la clase que define la meta-informacion del formulario
    class Meta:
        #De que modelo se basa este formulario
        model = Categoria

        #Que campos se van a ver en el formulario
        fields = ['nombre','imagen']

        #Personalizar la apariencia del formulario(widgets)

        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Nombre de la categoria'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Imagen del producto'
                }
            )
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen'
        }

        #Mensajes de error
        error_messages = {
            'nombre':{
                'required': 'El nombre es requerido'
            },
        }