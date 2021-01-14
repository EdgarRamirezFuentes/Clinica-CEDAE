from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from ..gestion_usuarios.models import Usuario
from ..gestion_pacientes.models import Paciente
from ..gestion_medicos.models import Medico
from ..gestion_farmacia.models import Encargado_farmacia
from django.contrib import messages
import hashlib

'''
class Home(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        self.request.session['id_medico'] = ""
        return context
'''

class Home(TemplateView):
    template_name = 'home/home.html'
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_paciente', False):
            ## Aquí va la redirección a la interfaz home paciente, si tan solo tuvieramos una
            pass
        else:
            return super().get(*args, **kwargs)

class Login(TemplateView):
    template_name = 'home/login.html'
    
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_paciente', False):
            ## Aquí va la redirección a la interfaz home paciente, si tan solo tuvieramos una
            pass
        else:
            return super().get(*args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            correo = request.POST['correo'].strip(),
            contrasenia = request.POST['contrasenia'].strip(),
            encoder = hashlib.new("sha1", str(contrasenia[0]).encode('utf-8'))
            contrasenia = str(encoder.hexdigest()) 
            tipo = request.POST['tipo'].strip(),
            usuario = None
            medico = None
            paciente = None
            try:
                usuario = Usuario.objects.get(correo=str(correo[0]))
            except Usuario.DoesNotExist as ex:
                messages.error(request, "El correo ingresado no pertenece a ninguna cuenta")
            if usuario:
                if str(tipo[0]) == 'medico':
                    try:
                        medico = Medico.objects.get(empleado_id_id=usuario.curp)
                    except Medico.DoesNotExist as ex:
                        messages.error(request, 'No existe un médico con el correo electrónico ingresado')
                    if medico:
                        if usuario.contrasenia == contrasenia:
                            request.session['id_medico'] = usuario.curp
                            return redirect('homeMedico')
                        else:
                            messages.error(request, 'La contraseña ingresada no es correcta')
                if str(tipo[0]) == 'encargado':
                    try:
                        encargado = Encargado_farmacia.objects.get(empleado_id_id=usuario.curp)
                    except Encargado_farmacia.DoesNotExist as ex:
                        messages.error(request, 'No existe un encargado de farmacia con el correo electrónico ingresado')
                    if encargado:
                        if usuario.contrasenia == contrasenia:
                            request.session['id_encargado'] = usuario.curp
                            return redirect('homefarmacia')
                        else:
                            messages.error(request, 'La contraseña ingresada no es correcta')
                #elif tipo == 'paciente':
                #   request.session['id_paciente'] = usuario.curp
                # Aquí redireccionaría a interfaz paciente, si tan solo tuvieramos una
        return redirect('login')

class Logout(TemplateView):
    template_name = 'home/home.html'
    def get(self, *args, **kwargs):
        self.request.session.flush()
        return redirect('home')
    

class AboutUs(TemplateView):
    template_name = 'home/aboutUs.html'
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_paciente', False):
            ## Aquí va la redirección a la interfaz home paciente, si tan solo tuvieramos una
            pass
        else:
            return super().get(*args, **kwargs)

class primera_cita(TemplateView):
    template_name = 'home/primera_cita.html'
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_paciente', False):
            ## Aquí va la redirección a la interfaz home paciente, si tan solo tuvieramos una
            pass
        else:
            return super().get(*args, **kwargs)

class contact_us(TemplateView):
    template_name = 'home/contact_us.html'
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_paciente', False):
            ## Aquí va la redirección a la interfaz home paciente, si tan solo tuvieramos una
            pass
        else:
            return super().get(*args, **kwargs)