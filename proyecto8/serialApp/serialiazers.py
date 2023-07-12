from rest_framework import serializers
from .models import Estudiante

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'