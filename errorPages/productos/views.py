from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Producto
from .serializers import ProductoSerializer
from .forms import productoForm
from django.shortcuts import render

def agregar (request):
    form=productoForm()
    return render (
        request,'agregar.html',
        {'form':form},status=200
    )


class ProductoViewset(viewsets.ModelViewSet):
    #Conjunto de query´s de la BD
    queryset=Producto.objects.all()
    
    #Saber como empaquetar a enviar la infromacion
    serializer_class=ProductoSerializer
    #Saber como voy a renderizar las respuestas
    renderer_classes=[JSONRenderer]

    #http_method_names=['GET','POST']