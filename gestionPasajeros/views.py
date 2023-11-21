
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from gestionPasajeros.models import Aeropuerto, Vuelo, Pasajero

# Create your views here.
class AeropuertoListView(ListView):
    model = Aeropuerto

class AeropuertoDetailView(DetailView):
    model = Aeropuerto

class VueloListView(ListView):
    model = Vuelo

class VueloDetailView(DetailView):
    model = Vuelo

class PasajeroListView(ListView):
    model = Pasajero

class PasajeroDetailView(DetailView):
    model = Pasajero