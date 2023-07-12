from django.http import HttpResponse
from django.shortcuts import render
from gestionPedido_App.models import Productos
# Create your views here.
def busqueda(request):
    return render(request, "busqueda_producto.html")

def buscar(request):
    if request.GET["prod"]:
        # mensaje = "Producto buscado: %r" %request.GET["prod"]
        producto = request.GET["prod"]
        if len(producto)>20:
            mensaje = "Texto de busqueda demasiado largo"
        else:    
            prod = Productos.objects.filter(nombre__icontains = producto)
            return render(request, "resultado.html",{"producto": prod,"query": producto})
    else:
        mensaje = "No has introducido nada"
    return HttpResponse(mensaje)