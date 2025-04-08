from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse
import json
def agregar_categorias(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista') 
    
    else: 
        form = categoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_categorias2(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista') 
    
    else: 
        form = categoriaForm()
    return render(request, 'agregar_async.html', {'form': form})

def ver_categorias(request):
    categorias = Categoria.objects.all()
    #Esramos devolviendo al front un objeto desde el back
    return render(request, 'lista_categorias.html', {'categorias': categorias})

#esta funcion pinta el html que carga los productos con JSON

def index(request):
    return render(request, 'categorias.html')

def lista_categorias(request):
    categorias = Categoria.objects.all()

    #Generar un diccionario al aire que ordene los productos
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }

        for c in categorias
    ]

    return JsonResponse(data, safe=False)


def registrar_categorias(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Función que toma texto crudo y lo convierte a JSON
            categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )  # Estamos construyendo la instancia y guardándola en la BD
            return JsonResponse({
                'mensaje': 'Registro exitoso!',
                'id': categoria.id
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'Error': 'Ocurrió un error: ' + str(e)
            }, status=400)
    return JsonResponse({
        'Error': 'Método no soportado'
    }, status=405)


