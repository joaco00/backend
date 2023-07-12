from django.shortcuts import redirect, render
from socios_App.models import Socio
from socios_App.forms import FormSocio

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listasocio(request):
    soci = Socio.objects.all()
    data = {'socios': soci}
    return render(request, 'listadosocios.html', data)


def agregarsocio(request):
    form = FormSocio()
    if request.method == 'POST':
        form = FormSocio(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarsocio.html', data)

def eliminarsocio(request, id):
    soci = Socio.objects.get(id = id)
    soci.delete()
    return redirect('/listadosocios')

def actualizarsocio(request, id):
    soci = Socio.objects.get(id = id)
    form = FormSocio(instance=soci)
    if request.method == 'POST':
        form = FormSocio(request.POST, instance=soci)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarsocio.html', data)