from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
import datetime
from datetime import date, datetime
from ..gestion_pacientes.models import Consulta
from ..gestion_farmacia.models import Ticket


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

class pago(ListView):
    template_name ='gestion_recepcion/pago.html'
    model = Consulta
    context_object_name = 'consultas'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            listaSKU = []
            x = 1
            for i in request.POST:
                if x % 2 == 0:
                    listaSKU.append(i)
                x = x+1
            consu = Consulta.objects.get(id = listaSKU[0])

            ticket = Ticket(
                    medicamentos = listaSKU[0] + '. Consulta',
                    costo_total = consu.costo,
                    precioProducto = consu.costo,
                    fecha_expedicion = datetime.now(),
            )
            try:
                ticket.save()
                messages.success(request, 'Se registró correctamente el ticket')
            except Exception as ex:
                messages.error(request, 'Hubo un error al tratar de registrar el ticket', 'error')
        return redirect('ticket')
