from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse
from .forms import productoForms
import json 


# Create your views here.
def lista_productos(request):
    #Obtener todos los objetos de productos de la base de datos
    productos = Producto.objects.all();
    #Guardar los datos en un diccionario
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
            
    ]
    
    return JsonResponse(data, safe = False)

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ver.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = productoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = productoForms()
    return render(request, 'agregar.html', {'form': form})

def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )
            return JsonResponse(
                {'mensaje': 'Producto registrado correctamente',
                 'id': producto.id,
                 },
                status = 201
                                )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'mensaje': 'Error al registrar el producto'},
                status = 400
            )
    return JsonResponse(
        {'mensaje': 'Error método no esta soportado'},
        status = 405
    )