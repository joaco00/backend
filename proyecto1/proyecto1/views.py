import datetime
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Chao")

def muestrafecha(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse(fecha_actual)

def calcularEdad(request,edad_actual,agno):
    periodo = agno - 2022
    edadFutura = edad_actual + periodo    

    return HttpResponse("""<html>
                        <body>
                            <h2> En el año %s tendras %s años.</h2>
                        </body>
                    </html>""" %(agno, edadFutura))