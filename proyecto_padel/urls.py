"""
URL configuration for proyecto_padel project.

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
from app_padel import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='login'),
    path('login/', views.login_app, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('reserva_pista/<int:pista_id>/', views.reserva_pista, name='reservaPista'),
    path('mis_reservas/', views.misReservas, name='misReservas'),
    path('delete/<int:reserva_id>/', views.delete_reserva, name='delete'),
    path('clubs_disponibles/', views.clubs_disponibles, name='clubsDisponibles'),
    path('usuario/', views.usuario, name='usuario'),
    path('gestionar_detalles_club/<int:club_id>/', views.gestionar_detalles_club, name='gestionar_detalles_club'),
    path('modificar_club/<int:club_id>/', views.modificar_club, name='modificar_club'),
    path('administrar_club/', views.administrar_club, name='administrar_club'),
    path('crear_club/', views.crear_club, name='crearClub'),
    path('buscar_usuarios/', views.buscar_usuarios, name='buscar_usuarios'),
]
