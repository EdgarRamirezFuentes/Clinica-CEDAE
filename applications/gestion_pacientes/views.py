from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
import datetime
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from ..gestion_pacientes.models import Paciente 
from ..gestion_usuarios.models import Usuario
from ..gestion_pacientes.models import Cita
from ..gestion_pacientes.models import Receta
from ..gestion_pacientes.models import Cita
from ..gestion_pacientes.models import Consulta
from ..gestion_expediente.models import Expediente

# Create your views here.

class Home(TemplateView):
    template_name = 'gestion_pacientes/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(paciente_id_id=self.request.session['id_paciente'],
                                               fecha=datetime.date.today()
                                               ).order_by('hora_inicio')
        return context

class verPerfilPaciente(DetailView):
    template_name = 'gestion_pacientes/perfil.html'
    model = Paciente
    context_object_name = 'paciente'

class verExpediente(TemplateView):
    template_name = 'gestion_pacientes/verexpediente.html'

    def get_context_data(self, **kwargs):
        context = super(verExpediente, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(paciente_id = self.kwargs.get('pk'))
        context['consultas'] = Consulta.objects.filter(expediente_id = self.kwargs.get('pk'))
        context['recetas'] = Receta.objects.filter()
        context['expediente'] = Expediente.objects.get(pk = self.kwargs.get('pk'))
        return context
        
class cambiarContraseña(TemplateView):
    template_name = 'gestion_pacientes/modcontraseña.html'

class nuevaContraseña(TemplateView):
    template_name = 'gestion_pacientes/nuevacontraseña.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            usuario = Usuario.objects.get(curp = self.kwargs.get('pk'))
            usuario.contrasenia = request.POST['newPass']
            try:
                usuario.save()
                messages.success(request, 'Contraseña modificada correctamente')
            except Exception as es:
                messages.error(request, 'Hubo un error al intentar modificar la contraseña')
        return redirect('homePaciente')
        