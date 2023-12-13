from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)
from gestionPasajeros.models import Aeropuerto, Vuelo, Pasajero
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.

# Homo - Principal

def home(request):
    return render(request, "home.html")

# Aeropuertos
class AeropuertoListView(ListView):
    model = Aeropuerto
    template_name = 'aeropuerto_list.html'
    context_object_name = 'object_list'


class AeropuertoDetailView(DetailView):
    model = Aeropuerto
    template_name = 'aeropuerto_detail.html'
    context_object_name = 'aeropuerto'


def crear_aeropuerto(request):
    if request.method == 'POST':
        form = AeropuertoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aeropuerto-list')  # Redirige a la lista de aeropuertos después de crear uno nuevo
    else:
        form = AeropuertoForm()

    return render(request, 'crear_aeropuerto.html', {'form': form})


class AeropuertoUpdate(UpdateView):
    model = Aeropuerto
    template_name = 'aeropuerto_form.html'  # Puedes reutilizar el mismo formulario que usas para crear
    fields = ['codigo', 'nombre', 'ciudad', 'foto_aeropuerto']

class AeropuertoCreate(CreateView):
    model = Aeropuerto
    fields = "__all__"

class AeropuertoDelete(DeleteView):
    model = Aeropuerto
    template_name = 'aeropuerto_confirm_delete.html'
    success_url = reverse_lazy('aeropuerto-list')


# Vuelos

class VueloListView(ListView):
    model = Vuelo
    template_name = 'vuelo_list.html'
    context_object_name = 'object_list'

class VueloDetailView(DetailView):
    model = Vuelo
    template_name = 'vuelo_detail.html'
    context_object_name = 'object_list'


def crear_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vuelo-list')  # Reemplaza 'vuelo-list' con el nombre correcto de tu vista de lista de vuelos
    else:
        form = VueloForm()
    return render(request, 'crear_vuelo.html', {'form': form})


class VueloUpdate(UpdateView):
    model = Vuelo
    template_name = 'vuelo_form.html'
    fields = "__all__"
    

class VueloCreate(CreateView):
    model = Vuelo
    fields = "__all__"

class VueloDelete(DeleteView):
    model = Vuelo
    success_url = reverse_lazy("vuelo-list")



# Pasajeros

class PasajeroListView(ListView):
    model = Pasajero
    template_name = 'pasajero_list.html'
    context_object_name = 'object_list'


class PasajeroDetailView(DetailView):
    model = Pasajero
    template_name = 'pasajero_detail.html'
    context_object_name = 'object_list'


def crear_pasajero(request):
    if request.method == "POST":
        codigo_pasajero = request.POST["codigo_pasajero"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        celular = request.POST["celular"]
        correo = request.POST["correo"]
        num_vuelo = request.POST["num_vuelo"]
        # utilizando funcion create
        Pasajero.objects.create(
            codigo_pasajero=codigo_pasajero,
            nombre=nombre,
            apellido=apellido,
            celular=celular,
            correo=correo,
            num_vuelo=num_vuelo,
        )

    return render(request, "crear_pasajero.html")

class PasajeroUpdate(UpdateView):
    model = Pasajero
    template_name = 'pasajero_form.html'
    fields = "__all__"


class PasajeroCreate(CreateView):
    model = Pasajero
    fields = "__all__"


class PasajeroDelete(DeleteView):
    model = Pasajero
    success_url = reverse_lazy("pasajero-list")
    model = Pasajero



