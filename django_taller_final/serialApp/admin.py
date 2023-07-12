from django.contrib import admin

# Register your models here.
from serialApp.models import Inscritos,Institucion


class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre','fono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion']

admin.site.register(Inscritos, InscritosAdmin)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = []

admin.site.register(Institucion, InstitucionAdmin)