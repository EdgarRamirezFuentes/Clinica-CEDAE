from django.contrib import admin
from django.urls import path

def pruebaURL(self):
    print("================== Prueba desde gestión usuarios ==================")

urlpatterns = [
    path('usuarios/', pruebaURL,)
]
