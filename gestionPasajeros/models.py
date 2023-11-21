from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Selection(models.Model):
    """ seleccion de futbol  """
    name = models.CharField(max_length=50)
    shield = models.ImageField(upload_to='shields/')
    team = models.ImageField(upload_to='teams/')
    pub_date = models.DateField(auto_now_add=True)

  a  def __str__(self):
        return self.name

class Player(models.Model):
    """ Jugadores """
    selection = models.ForeignKey('Selection', on_delete=models.PROTECT,related_name='get_players' )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/')
    pub_date = models.DateField(auto_now_add=True)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
      # ----------------------------------------------------------------

class Aeropuerto(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo

class Vuelo(models.Model):
    numero_vuelo = models.CharField(max_length=10)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    codAeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.numero_vuelo

class Pasajero(models.Model):
    codigoPasajero = models.CharField(max_length=100)
    numero_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    def __str__(self):
        return self.codigoPasajero