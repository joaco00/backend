from rest_framework import serializers
from serialApp.models import Estudiante

class EstudianteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'