from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
import datetime
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from ..gestion_farmacia.models import Medicamento


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
    
class inventario(ListView):
    template_name = 'gestion_farmacia/inventario.html'
    model = Medicamento
    context_object_name = 'medicamentos'

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

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            medicamento = Medicamento(
                sku = request.POST['sku'],
                nombre = request.POST['nombre'],
                sustancia_activa = request.POST['sustancia_activa'],
                presentacion = request.POST['presentacion'],
                precio = float(request.POST['precio']),
                cantidad = int(request.POST['cantidad']),
                fecha_caducidad = request.POST['fecha_caducidad'],
                )
            try:
                medicamento.save()
                messages.success(request, 'Medicamento agregado correctamente')
            except Exception as ex:
                messages.error(request, 'Hubo un error al intentar agregar el medicamento')
        return redirect('/farmacia/inventario/')

class modmedicamento(TemplateView):
    template_name = 'gestion_farmacia/modmedicamento.html'

class ticket(TemplateView):
    template_name = 'gestion_farmacia/ticket.html'
