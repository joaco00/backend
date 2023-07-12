from django.db import models



# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaNacimiento = models.DateField()
    fono = models.CharField(max_length=12)
    email = models.EmailField()
    sexo = models.CharField( max_length=15)
    estado = models.CharField( max_length=15)