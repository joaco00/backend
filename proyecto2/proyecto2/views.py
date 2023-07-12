import datetime
from django.http import HttpResponse
from django.template import Template, Context


class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


def web(request):
    # nombre = "Joaquin"
    # apellido = "Anabalon"

    p1 = Persona("Joaquin", "Anabalon")

    fecha = datetime.datetime.now()

    doc_externo = open("proyecto2/web/miplantilla.html")

    plantilla = Template(doc_externo.read())

    doc_externo.close()

    cont = Context({"nom_persona": p1.nombre, "apel_persona": p1.apellido, "fecha_actual": fecha , "temas": ["Plantillas","Modelos","Formularios","Vistas"]})

    docu = plantilla.render(cont)   
    
    return HttpResponse(docu)
