from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('paciente/', views.Home.as_view(), name='homePaciente'),
    path('paciente/perfil/<pk>/', views.verPerfilPaciente.as_view(), name='patientProfilePatient'),
    path('paciente/expediente/<pk>/', views.verExpediente.as_view(), name='medicalRecord'),
    path('paciente/cambiar-contraseña/<pk>/', views.cambiarContraseña.as_view(), name='changePassword'),
]
