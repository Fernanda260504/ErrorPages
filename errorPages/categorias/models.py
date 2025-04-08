from django.db import models

# Create your models here.
class Categoria(models.Model):
    #Aqui va los atributos de mi clase
    nombre=models.CharField(max_length=100)
    #Que los campos urlfields limitan los caracteres a 200 por defecto
    imagen=models.URLField()

    def __str__(self):
        return self.nombre
    
    