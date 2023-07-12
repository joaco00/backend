from dataclasses import fields
from socket import fromshare
from django import forms
from socios_App.models import Socio

class FormSocio(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'