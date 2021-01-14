from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('administrador/home', views.Home.as_view(), name='homeAdmin'),
    path('administrador/', views.Login.as_view(), name='loginAdmin'),
    path('administrador/medicos', views.ListarMedicos.as_view(), name='medicosAdmin'),
    path('administrador/medicos/buscar/', views.ListarMedicosPorID.as_view(), name='searchDoctorsAdmin'),
    path('administrador/encargados-farmacia/', views.ListarEncargadosFarmacia.as_view(), name='encargadosAdmin'),
    path('administrador/encargados-farmacia/buscar/', views.ListarEncargadosPorID.as_view(), name='searchEncargadosAdmin'),
    #path('administrador/recepcionista', views.ListarRecepcionistas.as_view(), name='recepcionistasAdmin'),
    #path('administrador/pacientes', views.ListarPacientes.as_view(), name='pacientesAdmin'),
    
]
