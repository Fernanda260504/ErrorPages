from django.db import models

# Create your models here.
class Alumno(models.Model):
    #Aqui va los atributos de mi clase
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    edad=models.IntegerField()
    matricula=models.CharField(max_length=100,unique=True)
    correo=models.CharField(max_length=100,unique=True)
  
