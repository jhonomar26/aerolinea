from django import forms
from .models import *


class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = Aeropuerto
        fields = ["codigo", "nombre", "ciudad", "foto_aeropuerto"]

    def __init__(self, *args, **kwargs):
        super(AeropuertoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


# VUELOS
class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = "__all__"

    widgets = {
        "numero_vuelo": forms.TextInput(attrs={"class": "form-control"}),
        "origen": forms.TextInput(attrs={"class": "form-control"}),
        "destino": forms.TextInput(attrs={"class": "form-control"}),
        "cod_aeropuerto": forms.Select(attrs={"class": "form-control"}),
    }

    labels = {
        "numero_vuelo": "Número de Vuelo",
        "origen": "Origen",
        "destino": "Destino",
        "cod_aeropuerto": "Código de Aeropuerto",
    }


class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = "__all__"

    # Agrega clases de Bootstrap a los campos del formulario
    widgets = {
        "codigo_pasajero": forms.TextInput(attrs={"class": "form-control"}),
        "nombre": forms.TextInput(attrs={"class": "form-control"}),
        "apellido": forms.TextInput(attrs={"class": "form-control"}),
        "celular": forms.TextInput(attrs={"class": "form-control"}),
        "correo": forms.EmailInput(attrs={"class": "form-control"}),
        "num_vuelo": forms.Select(attrs={"class": "form-control"}),
    }
