from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('medico/', views.Home.as_view(), name='homeMedico'),
    path('medico/calendario/', views.Calendar.as_view(), name='calendarMedico'),
    path('medico/pacientes/', views.listarPacientes.as_view(), name='patientsMedico'),
    path('medico/pacientes/buscar/', views.listarPacientePorID.as_view(), name='searchPatientsMedico'),
    path('medico/registrar-paciente/', views.RegisterPatient.as_view(), name='registerPatientMedico'),
    path('medico/perfil-paciente/<pk>/', views.verPerfilPaciente.as_view(), name='patientProfileMedico'),
    path('medico/cita/<pk>/', views.appointment.as_view(), name='appointmentMedico'),
    path('medico/expediente-medico/<pk>/', views.verExpedientePaciente.as_view(), name='medicalRecordMedico'),
    path('medico/modificar-expediente/<pk>/', views.modificarExpediente.as_view(), name='modifyMedicalRecordMedico'),
]
