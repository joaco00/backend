from pyexpat import model
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha  = models.DateField()
    entregado = models.BooleanField()

# python manage.py shell

# from gestionPedido_App.models import Productos
#  pro = Productos(nombre = "mesa", categoria = "mueble",precio = 1000)
#pro.save()