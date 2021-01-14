from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import datetime


class Home(TemplateView):
    template_name = 'gestion_recepcion/home.html'

class primera_citar(TemplateView):
    template_name = 'gestion_recepcion/primera_citar.html'

class nueva_cita(TemplateView):
    template_name = 'gestion_recepcion/nueva_cita.html'

class agenda(TemplateView):
    template_name ='gestion_recepcion/agenda.html'

class ver_cita(TemplateView):
    template_name ='gestion_recepcion/ver_cita.html'

class pago(TemplateView):
    template_name ='gestion_recepcion/pago.html'
