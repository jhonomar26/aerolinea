
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from gestionPasajeros.models import Aeropuerto, Vuelo, Pasajero
from django.shortcuts import render
# Create your views here.
class AeropuertoListView(ListView):
    model = Aeropuerto

class AeropuertoDetailView(DetailView):
    model = Aeropuerto

def crear_aeropuerto(request):

    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        foto_aeropuerto  = request.POST['foto_aeropuerto']
        #utilizando funcion create
        Aeropuerto.objects.create(codigo=codigo, nombre=nombre, ciudad=ciudad, foto_aeropuerto=foto_aeropuerto)
       # 2 instanciar el objeto
        #aeropuerto = Aeropuerto()
        #aeropuerto.codigo = codigo
        #aeropuerto.nombre = nombre 
        #aeropuerto.ciudad = ciudad
        #aeropuerto.foto_aeropuerto = foto_aeropuerto 
        #aeropuerto.save()
    return render(request,'c:/aereo/gestionPasajeros/templates/gestionPasajeros/crear_aeropuerto.html')


def crear_vuelo(request):
     if request.method == 'POST':
        numero_vuelo = request.POST['numero_vuelo']
        origen = request.POST['origen']
        destino = request.POST['destino']
        cod_aeropuerto  = request.POST['cod_aeropuerto']
        #utilizando funcion create
        Vuelo.objects.create(numero_vuelo=numero_vuelo, origen=origen, destino=destino, cod_aeropuerto=cod_aeropuerto)

     return render(request,'c:/aereo/gestionPasajeros/templates/gestionPasajeros/crear_vuelo.html')


def crear_pasajero(request):
     if request.method == 'POST':
        codigo_pasajero = request.POST['codigo_pasajero']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        celular = request.POST['celular']
        correo = request.POST['correo']
        num_vuelo = request.POST['num_vuelo']
        #utilizando funcion create
        Pasajero.objects.create(codigo_pasajero=codigo_pasajero, nombre=nombre, apellido=apellido, celular=celular, correo=correo, num_vuelo=num_vuelo )

     return render(request,'c:/aereo/gestionPasajeros/templates/gestionPasajeros/crear_pasajero.html')

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
    model = Pasajero
