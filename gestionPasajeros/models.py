from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

"""
class Selection(models.Model):
    
    name = models.CharField(max_length=50)
    shield = models.ImageField(upload_to='shields/')
    team = models.ImageField(upload_to='teams/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    
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
    
    """
# ----------------------------------------------------------------


class Aeropuerto(models.Model):
    """Aeropuertos"""

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    foto_aeropuerto = models.ImageField(upload_to="foto_aeropuerto/")

    def __int__(self):
        return self.codigo

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("aeropuerto-list")
    
    


class Vuelo(models.Model):
    """Vuelos"""

    numero_vuelo = models.IntegerField(unique=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    cod_aeropuerto = models.ForeignKey(
        Aeropuerto, on_delete=models.PROTECT, related_name="get_vuelos"
    )

    def __int__(self):
        return self.numero_vuelo

    def __str__(self):
        return self.origen + " " + self.destino

    def get_absolute_url(self):
        return reverse("vuelo-list")


class Pasajero(models.Model):
    """Pasajeros"""

    codigo_pasajero = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.IntegerField()
    correo = models.CharField(max_length=100)
    num_vuelo = models.ForeignKey(
        Vuelo, on_delete=models.PROTECT, related_name="get_pasajeros"
    )

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("pasajero-list")
