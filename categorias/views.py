from django.shortcuts import render, redirect
from .forms import categoriaForm
from .models import Categoria
from django.http import JsonResponse


# Create your views here.
def agregar_categoria(request):
    if request.method == "POST":
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jsonCategorias")
    form = categoriaForm()
    return render(request, "registrarCategoria.html", {"form": form})


def get_categorias_json(request):
    categorias = Categoria.objects.all()

    json = [
        {
            "nombre": c.nombre,
            "imagen": c.imagen,
        }
        for c in categorias
    ]
    return JsonResponse(json, safe=False)


# Renderizar la vista de JSON
def json_view(request):
    return render(request, 'jsonCategorias.html')


import json
#Función que agrega un producto con un objeto JSON
def registrar_categoria(request):
    #Checa si muestra request es de tipo POST
    if request.method == 'POST':
        #quiere decir que si estoy manejando el request
        try:
            data = json.loads(request.body) #Parametro es un texto que debería ser un JSON
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            ) #Create directamente mete el objeto en la BD
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': categoria.id    
                }, status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status = 400
            )
    #Si no es POST el request...
    return JsonResponse (
        {'error': 'El método no es soportado'}, status = 405
    )
