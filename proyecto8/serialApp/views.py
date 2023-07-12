from django.shortcuts import render
from .serialiazers import EstudiantesSerializer
from .models import Estudiante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class ListarEstudiante(APIView):

    def get(self, request):
        estu = Estudiante.objects.all()
        serial = EstudiantesSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = EstudiantesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleEstudiante(APIView):

    def get_object(self, pk):
        try:
            return Estudiante.objects.get(pk=pk)
        except Estudiante.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = EstudiantesSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = EstudiantesSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



