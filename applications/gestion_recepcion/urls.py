from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('recepcion/', views.Home.as_view(), name='homerecepcion'),
    path('recepcion/primera_citar', views.primera_citar.as_view(), name='primera_citar'),
    path('recepcion/nueva_cita', views.nueva_cita.as_view(), name='nueva_cita'),   
    path('recepcion/agenda', views.agenda.as_view(), name='agenda'),
    path('recepcion/buscar-cita/', views.BuscarCita.as_view(), name='buscarCita'),
    path('recepcion/ver_cita', views.ver_cita.as_view(), name='ver_cita'),
    path('recepcion/pago', views.pago.as_view(), name='pago'),
]  
