from django.urls import path
from .views import *

urlpatterns = [
    path('json/', lista_categorias, name='listaCat'),
    path('api/get/', ver_categorias, name='verCat'),
    path('registrar/', agregar_categorias, name='agregarCat'),
]