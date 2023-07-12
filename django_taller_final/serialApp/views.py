from django.shortcuts import render,redirect
from serialApp.models import Inscritos,Institucion
from serialApp.forms import FormInscritos
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .serialiazers import InscritosSerializer,InstitucionSerializer
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return render(request, "index.html")

# Página de inicio

def listarReservas(request):
    inscri = Inscritos.objects.all()
    data = {'inscritos': inscri}
    return render(request, 'listado_reservas.html', data)


def agregarReservas(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_reserva.html', data)

def eliminarReservas(request, id):
    inscri= Inscritos.objects.get(id = id)
    inscri.delete()
    return redirect('/listadoreservas')

def actualizarReservas(request, id):
    inscri= Inscritos.objects.get(id = id)
    form = FormInscritos(instance=inscri)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=inscri)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_reserva.html', data)


#API REST
def verInscritos(request):
    inscri = Inscritos.objects.all()
    data = {'inscritos' : list(inscri.values('id','nombre', 'fono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion'))}
    return JsonResponse(data)

#Class View

class ListarInscritos(APIView):

    def get(self, request):
        inscri = Inscritos.objects.all()
        serial = InscritosSerializer(inscri, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleInscrito(APIView):

    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritosSerializer(inscri)
        return Response(serial.data)

    def put(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritosSerializer(inscri, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        inscri = self.get_object(pk)
        inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#FUNCTION BASED VIEWS
@api_view (['GET','POST'])
def ListaInstitucion(request):
    if request.method == 'GET':
        ins = Institucion.objects.all()
        serial = InstitucionSerializer(ins, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def DetalleInstitucion(request,pk):
    try:
        ins = Institucion.objects.get(id=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serial = InstitucionSerializer(ins)
        return Response(serial.data)


    if request.method == 'PUT':
        serial = InstitucionSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
