from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse
# Create your views here.
def agregar_producto(request):
    #checar si vengo desde el formulario enviado
    if request.method == 'POST':
        #mandaron el formulario
        form = productoForm(request.POST)
        #validar que el formulario este correcto
        if form.is_valid():
            #si es valido entonces lo guardo
            form.save()
            return redirect('ver') #redirecciona a la lista de productos
    #si no vengo de enviar el formulario
    else: 
        form = productoForm()
    #vamos a pintar el formulario
    return render(request, 'agregar_productos.html', {'form': form})



#función que agrega productos desde una llamada asincrona
import json
#etiqueta para vitar el uso de CSRF
#@csrf_exempt <-- Evitar su uso a menos que estemos probando

def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Función que toma texto crudo y lo convierte a JSON
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            )  # Estamos construyendo la instancia y guardándola en la BD
            return JsonResponse({
                'mensaje': 'Registro exitoso!',
                'id': producto.id
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'Error': 'Ocurrió un error: ' + str(e)
            }, status=400)
    return JsonResponse({
        'Error': 'Método no soportado'
    }, status=405)



def ver_producto(request):
    #Obtener de la BD todos los productos
    productos = Producto.objects.all()
    #Esramos devolviendo al front un objeto desde el back
    return render(request, 'ver.html', {'productos': productos})

#esta funcion pinta el html que carga los productos con JSON
def index(request):
    return render(request, 'productos.html')

#Devolver todos los productos como un JSON
def lista_productos(request):
    productos = Producto.objects.all()

    #Generar un diccionario al aire que ordene los productos
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }

        for p in productos
    ]

    return JsonResponse(data, safe=False)