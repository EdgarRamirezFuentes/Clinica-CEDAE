from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('administrador/home', views.Home.as_view(), name='homeAdmin'),
    path('administrador/', views.Login.as_view(), name='loginAdmin'),
]
