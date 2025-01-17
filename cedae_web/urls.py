"""cedae_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluyendo urls de la app home
    re_path('', include('applications.home.urls')),
    # Incluyendo urls de la app gestion_usuarios
    re_path('', include('applications.gestion_usuarios.urls')),
    # Incluyendo urls de la app gestion_pacientes
    re_path('', include('applications.gestion_pacientes.urls')),
    # Incluyendo urls de la app gestion_medicos
    re_path('', include('applications.gestion_medicos.urls')),
    # Incluyendo urls de la app gestion_farmacia
    re_path('', include('applications.gestion_farmacia.urls')),
    # Incluyendo urls de la app gestion_recepcion
    re_path('', include('applications.gestion_recepcion.urls')),
    # Incluyendo urls de la app gestion_empleados
    re_path('', include('applications.gestion_empleados.urls')),
    # Incluyendo urls de la app gestion_expediente
    re_path('', include('applications.gestion_expediente.urls')),
    # Incluyendo urls de la app gestion_admin
    re_path('', include('applications.gestion_admin.urls')),
]
