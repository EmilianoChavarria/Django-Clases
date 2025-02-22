from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForms


# Create your views here.
def lista_categorias(request):
    #Obtener todos los objetos de productos de la base de datos
    categorias = Categoria.objects.all();
    #Guardar los datos en un diccionario
    data = [
        {
            'nombre': p.nombre,
            'imagen': p.imagen
        }
        for p in categorias
            
    ]
    
    return JsonResponse(data, safe = False)

def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'verCat.html', {'categorias': categorias})


def agregar_categorias(request):
    if request.method == 'POST':
        form = categoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verCat')
    else:
        form = categoriaForms()
    return render(request, 'agregarCat.html', {'form': form})