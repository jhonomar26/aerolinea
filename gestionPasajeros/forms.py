from django import forms
from .models import *

class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = Aeropuerto
        fields = ['codigo', 'nombre', 'ciudad', 'foto_aeropuerto']

    def __init__(self, *args, **kwargs):
        super(AeropuertoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['numero_vuelo', 'origen', 'destino', 'cod_aeropuerto']
