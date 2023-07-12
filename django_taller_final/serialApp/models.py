from django.db import models

estado = (
    ( 'Reservado','Reservado'),
    ( 'Completada','Completada'),
    ( 'Anulada','Anulada'),
    ( 'No asisten','No asisten'),
)


# Create your models here.
class Inscritos(models.Model):
    nombre = models.CharField(max_length=50)
    fono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=50)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=50,choices=estado,default="")
    observacion = models.TextField(max_length=50, null=True)

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)