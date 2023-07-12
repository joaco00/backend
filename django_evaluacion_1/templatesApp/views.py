from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def index(request):
    return render(request, 'templatesWeb/index.html')
#VISTA PAGINA ROPA    
def ropa(request):
    return render(request, 'templatesWeb/ropa.html')
#VISTA PAGINA JUGUETES
def juguetes(request):
    return render(request, 'templatesWeb/juguetes.html')

#VISTA PAGINA ELECTRONICA
def electronica(request):
    return render(request, 'templatesWeb/electronica.html')    

#USER CON HTTPRESPONSE
def user(request):
    doc_externo = open("plantillas/templatesWeb/user.html")

    plantilla = Template(doc_externo.read())

    doc_externo.close()

    cont = Context({"temas": ["DJANGO SHOP","Electronica","Juguetes","Ropa"]})

    docu = plantilla.render(cont)   
    
    return HttpResponse(docu)

