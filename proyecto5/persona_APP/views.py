from tkinter.tix import Form
from django.shortcuts import render, redirect
from persona_APP.models import Persona, Proyecto
from persona_APP.forms import FormProyecto

# Create your views here.
def persona(request):
    per = Persona.objects.all()
    data = {'persona' : per}
    return render(request, 'persona.html', data)

def index(request):
    return render(request, "index.html")

def listaproyecto(request):
    pro = Proyecto.objects.all()
    data = {'proyecto' : pro}
    return render(request, "listaproyecto.html", data)

def agregarproyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)

def eliminarproyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    pro.delete()
    return redirect('/listaproyecto')

def actualizarproyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=pro)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=pro)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)