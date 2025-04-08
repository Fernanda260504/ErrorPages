from django.db import models
from categorias.models import Categoria
# Create your models here. 
class Producto(models.Model):
    #Aqui va los atributos de mi clase
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    #Que los campos urlfields limitan los caracteres a 200 por defecto
    imagen=models.URLField()

    #Agregar una relacion con categoria
    #Parametros:Modelo
    categoria=models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
         null=True,
         blank=True


                                
     ) # type: ignore

    def __str__(self):
        return self.nombre