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
import hashlib

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
        context['acceso'] = Paciente.objects.values('accesoExpediente').get(pk = self.kwargs.get('pk'))
        return context
        
class cambiarContraseña(TemplateView):
    template_name = 'gestion_pacientes/modcontraseña.html'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            usuario = Usuario.objects.get(curp = self.kwargs.get('pk'))
            contraseniaNueva = request.POST['passNueva'].strip()
            print(contraseniaNueva)
            encoder = hashlib.new("sha1", str(contraseniaNueva).encode('utf-8'))
            contraseniaNueva = str(encoder.hexdigest()) 
            print(contraseniaNueva)
            usuario.contrasenia = contraseniaNueva
            try:
                usuario.save()
                send_mail(
                'Cambio de contraseña exitoso',
                'Tu cambio de contraseña ha sido exitoso',
                settings.EMAIL_HOST_USER,
                [usuario.correo,],
                fail_silently = False,
                )
                messages.success(request, 'Contraseña modificada correctamente')
            except Exception as es:
                messages.error(request, 'Hubo un error al intentar modificar la contraseña')
        return redirect('homePaciente')

