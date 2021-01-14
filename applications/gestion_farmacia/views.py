from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
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

class infmedicamento(DetailView):
    template_name = 'gestion_farmacia/infmedicamento.html'
    model = Medicamento
    context_object_name = 'medicamento'

class surtircedae(TemplateView):
    template_name = 'gestion_farmacia/surtircedae.html'

class surtirpublico(TemplateView):
    template_name = 'gestion_farmacia/surtirpublico.html'

class agregarmedicamento(TemplateView):
    template_name = 'gestion_farmacia/agregarmedicamento.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            med = Medicamento.objects.get(pk = self.kwargs.get('pk'))
            medicamento = Medicamento(
                sku = med,
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
        return redirect('inventario')

class modmedicamento(DetailView):
    template_name = 'gestion_farmacia/modmedicamento.html'
    model = Medicamento
    context_object_name = 'medicamento'

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
                messages.success(request, 'Medicamento modificado correctamente')
            except Exception as ex:
                messages.error(request, 'Hubo un error al intentar modificar el medicamento')
        return redirect('inventario')

class ticket(TemplateView):
    template_name = 'gestion_farmacia/ticket.html'
