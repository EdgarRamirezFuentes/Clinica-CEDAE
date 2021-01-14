from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
import datetime


class Home(TemplateView):
    template_name = 'gestion_farmacia/home.html'
    def get(self, *args, **kwargs):
        if self.request.session.get('id_encargado', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        else:
            messages.warning(self.request, 'Para ingresar a la página de encargado de farmacia debes iniciar sesion primero')
            return redirect('login')
    
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
