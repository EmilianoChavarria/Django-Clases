from django.urls import path
from .views import *

urlpatterns = [
    path('api/registrar/', agregar_categoria, name='registrar'), 
    path('api/get/', get_categorias_json, name='json_format'),
    path('json/', json_view, name='jsonCategorias'),
    path('api/post/', registrar_categoria, name='post'),
]