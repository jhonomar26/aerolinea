
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

class AeropuertoUpdate(UpdateView):
    model = Aeropuerto
    fields = '__all__' 

class AeropuertoCreate(CreateView):
    model = Aeropuerto
    fields = '__all__'

class AeropuertoDelete(DeleteView):
    model = Aeropuerto
    success_url = reverse_lazy('aeropuerto-list')

class VueloUpdate(UpdateView):
    model = Vuelo
    fields = '__all__' 

class VueloCreate(CreateView):
    model = Vuelo
    fields = '__all__'

class VueloDelete(DeleteView):
    model = Vuelo
    success_url = reverse_lazy('vuelo-list')



class PasajeroUpdate(UpdateView):
    model = Pasajero
    fields = '__all__' 

class PasajeroCreate(CreateView):
    model = Pasajero
    fields = '__all__'

class PasajeroDelete(DeleteView):
    model = Pasajero
    success_url = reverse_lazy('pasajero-list')
