from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from datetime import timedelta
from django.db.models import F
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
        
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['medicamentosACaducar'] = Medicamento.objects.filter(fecha_caducidad__lte = date.today() + timedelta(days=90))
        context['medicamentosATerminar'] = Medicamento.objects.filter(cantidad__lte = 20)
        return context
    
class inventario(ListView):
    template_name = 'gestion_farmacia/inventario.html'
    model = Medicamento
    context_object_name = 'medicamentos'
    
class BuscarMedicamentosPorNombre(ListView):
    template_name = 'gestion_farmacia/inventario.html'
    model = Medicamento
    context_object_name = 'medicamentos'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        queryset = Medicamento.objects.filter(
            nombre__icontains = nombre
        )
        return queryset

class surtirreceta(TemplateView):
    template_name = 'gestion_farmacia/surtirreceta.html'

class infmedicamento(DetailView):
    template_name = 'gestion_farmacia/infmedicamento.html'
    model = Medicamento
    context_object_name = 'medicamento'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            sk = request.POST['baja']
            med = Medicamento.objects.get(pk = sk)
            try:
                med.delete()
                messages.success(request, 'Medicamento eliminado correctamente')
            except Exception as es:
                messages.error(request, 'Hubo un error al intentar eliminar el medicamento')
        return redirect('inventario')

class surtircedae(TemplateView):
    template_name = 'gestion_farmacia/surtircedae.html'

class surtirpublico(ListView):
    template_name = 'gestion_farmacia/surtirpublico.html'
    model = Medicamento
    context_object_name = 'medicamentos'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            for i in request.POST:
                print(i)
            #l = request.POST['algo']
            pass
        redirect('ticket')

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
            pruebaExistencia = None
            try:
                pruebaExistencia = Medicamento.objects.get(sku = medicamento.sku)
                print(pruebaExistencia)
                messages.error(request, 'El SKU ingresado ya existe en el inventario')
            except Medicamento.DoesNotExist as ex:
                try:
                    medicamento.save()
                    messages.success(request, 'Medicamento agregado correctamente') 
                except Exception as ex:
                    messages.error(request, 'Hubo un error al intentar agregar el medicamento')
        return redirect('agregarmedicamento')

class modmedicamento(DetailView):
    template_name = 'gestion_farmacia/modmedicamento.html'
    model = Medicamento
    context_object_name = 'medicamento'

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
                messages.success(request, 'Medicamento modificado correctamente')
            except Exception as ex:
                messages.error(request, 'Hubo un error al intentar modificar el medicamento')
        return redirect('inventario')

class ticket(TemplateView):
    template_name = 'gestion_farmacia/ticket.html'
