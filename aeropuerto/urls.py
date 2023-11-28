"""
URL configuration for aeropuerto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionPasajeros import views

from django.urls import path
from django.views import *
urlpatterns = [
    # ruta home
    path('',views.home, name='ruta-home'),
    path('admin/', admin.site.urls),
    path('aeropuerto/', views.AeropuertoListView.as_view(), name='aeropuerto-list'),
    path('aeropuerto/<int:pk>/detail/', views.AeropuertoDetailView.as_view(), name='aeropuerto-detail'),
    path('vuelo/', views.VueloListView.as_view(), name='vuelo-list'),
    path('vuelo/<int:pk>/detail/', views.VueloDetailView.as_view(), name='vuelo-detail'),
    path('pasajero/', views.PasajeroListView.as_view(), name='pasajero-list'),
    path('pasajero/<int:pk>/detail/', views.PasajeroDetailView.as_view(), name='pasajero-detail'),
    # ruta crear aeropuerto
    path('aeropuerto/crear/', views.crear_aeropuerto, name='crear-aeropuerto'),
    # ruta crear vuelo
    path('vuelo/crear/',views.crear_vuelo, name='crear-vuelo'),
    # ruta crear pasajero
    path('pasajero/crear/',views.crear_pasajero, name='crear-pasajero'),

 # Update aeropuerto 
    path('aeropuerto/<int:pk>/update/',views.AeropuertoUpdate.as_view(),name='aeropuerto-update'), 
    #Create aeropuerto 
    path('aeropuerto/create/', views.AeropuertoCreate.as_view(), name='aeropuerto-create'),
    #Delete aeropuerto 
    path('aeropuerto/<int:pk>/delete/', views.AeropuertoDelete.as_view(), name='aeropuerto-delete'),
    
    # Update vuelo 
    path('vuelo/<int:pk>/update/',views.VueloUpdate.as_view(),name='vuelo-update'), 
    #Create vuelo 
    path('vuelo/create/', views.VueloCreate.as_view(), name='vuelo-create'),
    #Delete vuelo 
    path('vuelo/<int:pk>/delete/', views.VueloDelete.as_view(), name='vuelo-delete'),
    

    # Update pasajero
    path('pasajero/<int:pk>/update/',views.PasajeroUpdate.as_view(),name='pasajero-update'), 
    #Create pasajero
    path('pasajero/create/', views.PasajeroCreate.as_view(), name='pasajero-create'),
    #Delete pasajero
    path('pasajero/<int:pk>/delete/', views.PasajeroDelete.as_view(), name='pasajero-delete'),
    

]
