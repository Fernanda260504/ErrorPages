from django.shortcuts import render,redirect
from .models import Categoria
from .forms import categoriasForm
from django.http import JsonResponse
# Create your views here.
def agregar_categoria(request):
    #Checar si vengo desde el formulario enviado
    if request.method =='POST':
        #Mandaron el formulario
        form =categoriasForm(request.POST)
        #Validar que el formulario este correcto 
        if form.is_valid():
            #Si es valido entonces lo guardo
            form.save()
            return redirect('ver') #Redirecciona a la lista de categoria
    #Si no vengo de enviar el formulario (si solo quiero ver)
    else :
        form=categoriasForm()
    #Vamos a pintar el formulario
    return render(request,'agregar_categoria.html',{'form':form})    

def ver_categoria(request):
    #Obtener de la base de datos todoso los productos
    categoria=Categoria.objects.all()
    #Estamos de volviendo u front un obejto desde el back
    return  render (request,'ver_categoria.html',{'categorias':categoria})

#Esta funcion pinta el html que carga los productos con json
def index(request):
    return render(request,'categoria.html')

#esta funcion que devuelve todod los productos como un JSON
def lista_categoria(request):
    categoria=Categoria.objects.all()
     #Generar un diccionario al aire que ordena los productos

    data=[
         {
            'nombre':c.nombre,
            'imagen':c.imagen,
         }
         for c in categoria
     ]
    return JsonResponse(data,safe=False)
#Practica 18/02/2025
#función que agrega productos desde una llamada asincrona
import json
#etiqueta para vitar el uso de CSRF
#@csrf_exempt <-- Evitar su uso a menos que estemos probando

def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Función que toma texto crudo y lo convierte a JSON
            categorias = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )  # Estamos construyendo la instancia y guardándola en la BD
            return JsonResponse({
                'mensaje': 'Registro exitoso!',
                'id': categorias.id
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'Error': 'Ocurrió un error: ' + str(e)
            }, status=400)
    return JsonResponse({
        'Error': 'Método no soportado'
    }, status=405)