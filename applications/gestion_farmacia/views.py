from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import datetime


class Home(TemplateView):
    template_name = 'gestion_farmacia/home.html'
    
class inventario(TemplateView):
    template_name = 'gestion_farmacia/inventario.html'

class surtirreceta(TemplateView):
    template_name = 'gestion_farmacia/surtirreceta.html'

class infmedicamento(TemplateView):
    template_name = 'gestion_farmacia/infmedicamento.html'

class surtircedae(TemplateView):
    template_name = 'gestion_farmacia/surtircedae.html'

class surtirpublico(TemplateView):
    template_name = 'gestion_farmacia/surtirpublico.html'

class agregarmedicamento(TemplateView):
    template_name = 'gestion_farmacia/agregarmedicamento.html'

class modmedicamento(TemplateView):
    template_name = 'gestion_farmacia/modmedicamento.html'

class ticket(TemplateView):
    template_name = 'gestion_farmacia/ticket.html'
