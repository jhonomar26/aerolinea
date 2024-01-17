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
from django.urls import include
from gestionPasajeros import views
from accounts.urls import *

from django.urls import path
from django.views import *

from rest_framework import routers # importamos routers

#Creamos Routers o enlaces a la Appi
router = routers.DefaultRouter()
router.register(r'aeropuerto_rest', views.AeropuertoViewSet)# Cuando utilice la ruta aeropuerto_rest vaya a ese views
router.register(r'vuelo_rest', views.VueloViewSet)
router.register(r'pasajero_rest', views.PasajeroViewSet)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),  # nuevo
    path("accounts/", include("accounts.urls")), # nuevo
    # Local apps
    path("", include("pages.urls")),
    # ruta home
    path("home/", views.home, name="ruta-home"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
   # path("/", views.home, name="ruta-home"),
    # ruta Admin
    path("admin/", admin.site.urls),
  
    #----------------------------AEROPUERTOS-----------------------
    # Update aeropuerto
    path("aeropuerto/<int:pk>/update/", views.AeropuertoUpdate.as_view(), name="aeropuerto-update"),
    # Create aeropuerto
    path("aeropuerto/create/", views.crear_aeropuerto, name="aeropuerto-create"),
    # Lista aeropuerto
    path("aeropuerto/", views.AeropuertoListView.as_view(), name="aeropuerto-list"),
    # Detalle aeropuerto
    path("aeropuerto/<int:pk>/detail/", views.AeropuertoDetailView.as_view(), name="aeropuerto-detail"),
    # Crear Aeropuerto
    path("aeropuerto/crear/", views.crear_aeropuerto, name="crear-aeropuerto"),
    # Delete Aeropuerto
    path("aeropuerto/<int:pk>/delete/", views.AeropuertoDelete.as_view(), name="aeropuerto-delete"),
    
    #------------------------VUELOS-------------------------------

    # Update vuelo
    path("vuelo/<int:pk>/update/", views.VueloUpdate.as_view(template_name="vuelo_update.html"), name="vuelo-update"),
    # Create vuelo
    path("vuelo/create/", views.crear_vuelo, name="vuelo-create"),
    # Delete vuelo
    path("vuelo/<int:pk>/delete/", views.VueloDelete.as_view(template_name="vuelo_confirm_delete.html"), name="vuelo-delete"),
    path(
        "vuelo/",
        views.VueloListView.as_view(template_name="vuelo_list.html"),
        name="vuelo-list",
    ),
    path(
        "vuelo/<int:pk>/detail/", views.VueloDetailView.as_view(template_name="vuelo_detail.html"), name="vuelo-detail"
    ),
    path("vuelo/crear/", views.crear_vuelo, name="crear-vuelo"),

   #-----------------------------PASAJEROS---------------------------
   
    # Update pasajero
    
    
    
    path(
        "pasajero/<int:pk>/update/",
        views.PasajeroUpdate.as_view(template_name="pasajero_form.html"),
        name="pasajero-update",
    ),
    # Create pasajero
    path("pasajero/create/", views.PasajeroCreate.as_view(template_name="crear_pasajero.html"), name="pasajero-create"),
    # Delete pasajero
    path(
        "pasajero/<int:pk>/delete/",
        views.PasajeroDelete.as_view(template_name="pasajero_confirm_delete.html"),
        name="pasajero-delete",
    ),
    path("pasajero/crear/", views.crear_pasajero, name="crear-pasajero"),
    # Pasajero
    path("pasajero/", views.PasajeroListView.as_view(template_name="pasajero_list.html"), name="pasajero-list"),
    path(
        "pasajero/<int:pk>/detail/",
        views.PasajeroDetailView.as_view(template_name="pasajero_detail.html"),
        name="pasajero-detail",
    ),

    #Definición de routers, rutas de los serializers que se crearon
    
   path('', include(router.urls)),
   path('api/', include('rest_framework.urls', namespace='rest_framework')),
   
   path("api/", include("todos.urls")),  # nuevo

]
