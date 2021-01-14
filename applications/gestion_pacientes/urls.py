from django.contrib import admin
from django.urls import path

def pruebaURL(self):
    print("================== Prueba desde gestión pacientes ==================")

urlpatterns = [
    path('pacientes/', pruebaURL,)
]
