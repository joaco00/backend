from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout,login,authenticate
from bodega_App.forms import FormMovimiento, FormProducto
from bodega_App.models import Movimiento, Producto
from django.contrib.auth.decorators import login_required
# Create your views here.


# @login_required
# def home(request):
#     return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request,'interfazjefe.html',{'form':form})
        else:
            return render(request,'signup.html',{'form': form})
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form': form})

def signout(request):
    logout(request)
    return redirect("/")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and username == "admin":
            login(request, user)
            return redirect('/interfazjefe/')
            
        elif user is not None and username == username:
            login(request, user)
            return redirect('/interfazusuario/') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

# @login_required

def interfazusuario(request):
    return render(request, 'interfazusuario.html')


def agregarmovimiento(request):
    form = FormMovimiento()
    if request.method == 'POST':
        form = FormMovimiento(request.POST)
        if form.is_valid():
            form.save()
            return interfazusuario(request)
    data = {'form' : form }
    return render(request, 'agregarmovimiento.html', data)

        
def listarmovimiento(request):
    mov = Movimiento.objects.all()
    data = {'movimiento': mov}
    return render(request, 'listarmovimiento.html', data)

# @login_required
def interfazjefe(request):
    return render(request, 'interfazjefe.html')

def agregarproducto(request):
    form = FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            return interfazjefe(request)
    data = {'form' : form}
    return render(request, 'agregarproducto.html', data)

def listarproducto(request):
    pro = Producto.objects.all()
    data = {'producto': pro }
    return render(request, 'listarproducto.html', data)

def listarmovimientojefe(request):
    mov = Movimiento.objects.all()
    data = {'movimiento': mov}
    return render(request, 'listarmovimientojefe.html', data)

def eliminarproducto(request, id):
    pro = Producto.objects.get(id = id)
    pro.delete()
    return redirect('/productos')

def actualizarproducto(request, id):
    pro = Producto.objects.get(id = id)
    form = FormProducto(instance=pro)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return listarproducto(request)
    data = {'form': form}
    return render(request, 'agregarproducto.html', data)

def eliminarmovimiento(request, id):
    mov = Movimiento.objects.get(id = id)
    mov.delete()
    return redirect('/movimientosjefe')

def actualizarmovimiento(request, id):
    mov = Movimiento.objects.get(id = id)
    form = FormMovimiento(instance=mov)
    if request.method == 'POST':
        form = FormMovimiento(request.POST, instance=mov)
        if form.is_valid():
            form.save()
        return listarmovimientojefe(request)
    data = {'form': form}
    return render(request, 'agregarmovimiento.html', data)

def actualizarmovimientou(request, id):
    mov = Movimiento.objects.get(id = id)
    form = FormMovimiento(instance=mov)
    if request.method == 'POST':
        form = FormMovimiento(request.POST, instance=mov)
        if form.is_valid():
            form.save()
        return listarmovimiento(request)
    data = {'form': form}
    return render(request, 'agregarmovimiento.html', data)

