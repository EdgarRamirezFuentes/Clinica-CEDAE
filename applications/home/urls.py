from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name ='home'),
    path('iniciar-sesion/', views.Login.as_view(), name='login'),
    path('cerrar-sesion/', views.Logout.as_view(), name='logout'),
    path('acerca-de-nosotros/', views.AboutUs.as_view(), name='aboutUs'),
    path('primera_cita/', views.primera_cita.as_view(), name='primera_cita'),
    path('contact_us/', views.contact_us.as_view(), name='contact_us'),
]