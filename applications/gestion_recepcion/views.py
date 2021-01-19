from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
import datetime
from datetime import date, datetime
from ..gestion_pacientes.models import Consulta
from ..gestion_pacientes.models import Cita
from ..gestion_farmacia.models import Ticket
from ..gestion_pacientes.models import Paciente
from ..gestion_medicos.models import Medico

class Home(TemplateView):
    template_name = 'gestion_recepcion/home.html'

class primera_citar(TemplateView):
    template_name = 'gestion_recepcion/primera_citar.html'

class nueva_cita(TemplateView):
    template_name = 'gestion_recepcion/nueva_cita.html'

class agenda(TemplateView):
    template_name ='gestion_recepcion/agenda.html'
    
    def get_context_data(self, **kwargs):
        context = super(agenda, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(fecha__gte=date.today()).order_by('fecha', 'hora_inicio')
        context['medicos'] = Medico.objects.all().order_by('empleado_id__usuario_curp__apellidoPaterno')
        return context

class BuscarCita(ListView):
    template_name = 'gestion_recepcion/agenda.html'
    context_object_name = 'citas'
    
    def get_context_data(self, **kwargs):
        context = super(BuscarCita, self).get_context_data(**kwargs)
        context['medicos'] = Medico.objects.all().order_by('empleado_id__usuario_curp__apellidoPaterno')
        return context
    
    def get_queryset(self):
            medico = self.request.GET.get('medico', '')
            paciente = self.request.GET.get('curp', '')
            if len(paciente) == 0:
                queryset = Cita.objects.filter(
                    medico_id_id = medico,
                    fecha__gte = date.today()
                ).order_by('fecha', 'hora_inicio')
            else:
                queryset = Cita.objects.filter(
                    medico_id_id = medico,
                    paciente_id_id = paciente,
                    fecha__gte = date.today()
                ).order_by('fecha', 'hora_inicio')
            return queryset
    
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
                    medicamentos = '1. Consulta id: ' + listaSKU[0],
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
