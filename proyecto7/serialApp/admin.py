from django.contrib import admin
from serialApp.models import Estudiante
# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['name','email','carrera','puntos']

admin.site.register(Estudiante, EstudianteAdmin)