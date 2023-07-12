
from django.db import models
from bodega_App.choices import ciudades, categorias


# Create your models here.


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20, choices=categorias, default='Audifonos')
    stock = models.IntegerField()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    nombre_encargado = models.CharField(max_length=30)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    bodega_origen = models.CharField(max_length=50, choices=ciudades )
    bodega_destino = models.CharField(max_length=50, choices=ciudades)


    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
        ordering = ["nombre_encargado"]

    def __str__(self):
        txt = "Con fecha {0} se movio la cantidad de {1} {2}"
        return txt.format(self.fecha, self.producto.stock,self.producto.nombre)

    
