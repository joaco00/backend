from django import forms
from bodega_App.models import Producto, Movimiento

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FormMovimiento( forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['fecha','nombre_encargado','bodega_origen','bodega_destino','producto']

        widgets = {
            'fecha' : forms.SelectDateWidget()
            
        }

