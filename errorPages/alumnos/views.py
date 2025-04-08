from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializers import AlumnoSerializer
from django.shortcuts import render, redirect
from .forms import alumnoForm

class AlumnoViewset(viewsets.ModelViewSet):
    #Conjunto de query´s de la BD
    queryset=Alumno.objects.all()
    
    #Saber como empaquetar a enviar la infromacion
    serializer_class=AlumnoSerializer
    #Saber como voy a renderizar las respuestas
    renderer_classes=[JSONRenderer]

def crud(request):
    forms = alumnoForm()
    return render(request, 'Bautista_Maria.html', {'form': forms})
