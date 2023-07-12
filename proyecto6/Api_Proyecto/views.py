from django.shortcuts import render
from django.http import JsonResponse
from Api_Proyecto.models import Empleados
# Create your views here.
def verEmpleados(request):
    emp  ={
        'id' : 1234,
        'nombre' : 'Joaquin',
        'email' : 'joaquin00@gmail.com',
        'sueldo' : '1000000'
    }
    return JsonResponse(emp)

def verEmpleadosDB(request):
    emple = Empleados.objects.all()
    data = {'empleado' : list(emple.values('nombre', 'sueldo'))}
    return JsonResponse(data)