from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('farmacia/', views.Home.as_view(), name='homefarmacia'),
    path('farmacia/inventario/', views.inventario.as_view(), name='inventario'),
    path('farmacia/infmedicamento/<pk>/', views.infmedicamento.as_view(), name='infmedicamento'),
    path('farmacia/surtircedae/', views.surtircedae.as_view(), name='surtircedae'),
    path('farmacia/surtirpublico/', views.surtirpublico.as_view(), name='surtirpublico'),
    path('farmacia/agregarmedicamento/', views.agregarmedicamento.as_view(), name='agregarmedicamento'),
    path('farmacia/modmedicamento/', views.modmedicamento.as_view(), name='modmedicamento'),
    path('farmacia/ticket', views.ticket.as_view(), name='ticket'),
]  
