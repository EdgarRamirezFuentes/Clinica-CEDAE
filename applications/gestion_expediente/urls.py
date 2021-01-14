from django.contrib import admin
from django.urls import path

def pruebaURL(self):
    print("================== Prueba desde gestión de expedientes ==================")

urlpatterns = [
    path('expediente/', pruebaURL,)
]
