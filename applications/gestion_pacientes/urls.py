from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('paciente/', views.Home.as_view(), name='homePaciente'),
    path('medico/perfil/<pk>/', views.verPerfil.as_view(), name='patientProfile'),
    path('medico/expediente/<pk>/', views.verExpediente.as_view(), name='medicalRecord'),
]
