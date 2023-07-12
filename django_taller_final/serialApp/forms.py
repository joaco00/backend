from django import forms
from serialApp.models import Inscritos

class FormInscritos(forms.ModelForm):
    hora_inscripcion = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    class Meta:
        model = Inscritos
        fields= ['nombre','fono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion']

        widgets = {
            'fecha_inscripcion': forms.SelectDateWidget
        }
