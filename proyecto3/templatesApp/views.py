from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templatesWeb/index.html')

def plantillas(request):
    data = [{"nombre": "Joaquin" ,"apellido": "Anabalon" }]
    return render(request, 'templatesWeb/miplantilla.html',data)

def infoUsuario(request):
    data = {"id": 123, "nombre": "Clark", "apellido": "Kent","email": "abc123@gmail.com"}
    return render(request, 'templatesWeb/userInfoTemplate.html', data)