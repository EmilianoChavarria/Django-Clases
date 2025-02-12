from django.db import models

# Create your models here.

#Clase Producto
class Producto(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    #Funcion que devuelva el objeto qen forma de diccionario
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
    
