from rest_framework import serializers
from .models import Aeropuerto, Vuelo, Pasajero
#from gestionPasajeros.models import Aeropuerto, Vuelo, Pasajero

class AeropuertoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aeropuerto
        
        fields = ('codigo', 'nombre', 'ciudad', 'foto_aeropuerto') #Campos que quiero mostrar de mi base de datos

class VueloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vuelo
        fields = ('__all__')

class PasajeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasajero
        fields = ('__all__')
