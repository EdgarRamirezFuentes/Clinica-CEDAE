from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib import messages
import hashlib
from ..gestion_usuarios.models import Usuario
from ..gestion_pacientes.models import Paciente, Cita
from ..gestion_pacientes.models import Receta
from ..gestion_pacientes.models import Cita
from ..gestion_pacientes.models import Consulta
from ..gestion_expediente.models import Expediente
from ..gestion_medicos.models import Medico
from ..gestion_empleados.models import Empleado
from ..gestion_farmacia.models import Encargado_farmacia
from .models import Administrador

class Home(TemplateView):
    template_name = 'gestion_admin/home.html'
    
    ## Válida que esté logeado un admin
    def get(self, *args, **kwargs):
        if self.request.session.get('id_admin', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        else:
            messages.warning(self.request, 'Para ingresar a la página de administrador debes iniciar sesion primero')
            return redirect('loginAdmin')
    
class Login (TemplateView):
    template_name = 'gestion_admin/login.html'
    
    def get(self, *args, **kwargs):
        if self.request.session.get('id_admin', False):
            return redirect('homeAdmin')
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        else:
            return super().get(*args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            usuario = request.POST['usuario'].strip(),
            contrasenia = request.POST['contrasenia'].strip(),
            encoder = hashlib.new("sha1", str(contrasenia[0]).encode('utf-8'))
            contrasenia = str(encoder.hexdigest()) 
            admin = None
            try:
                admin = Administrador.objects.get(usuario= str(usuario[0]))
            except Administrador.DoesNotExist as ex:
                messages.error(request, "El usuario ingresado no existe")
            if admin:
                print(admin.usuario)
                print(admin.contrasenia)
                
                if admin.contrasenia == contrasenia:
                    request.session['id_admin'] = admin.usuario
                    return redirect('homeAdmin')
                else:
                    messages.error(request, "La contraseña ingresada no es correcta")
        return redirect('loginAdmin')
    
class ListarMedicos(ListView):
    template_name = 'gestion_admin/doctors.html'
    model = Medico
    context_object_name = 'medicos'
    
    def get(self, *args, **kwargs):
        if self.request.session.get('id_admin', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        elif self.request.session.get('id_medico', False):
            return redirect('homeMedico')
        else:
            messages.warning(self.request, 'Para ingresar a la página de administrador debes iniciar sesion primero')
            return redirect('loginAdmin')
        
class ListarMedicosPorID(ListView):
        template_name = 'gestion_admin/doctors.html'
        context_object_name = 'medicos'
        ## Válida que esté logeado un administrador
        def get(self, *args, **kwargs):
            if self.request.session.get('id_admin', False):
                return super().get(*args, **kwargs)
            elif self.request.session.get('id_encargado', False):
                return redirect('homefarmacia')
            elif self.request.session.get('id_medico', False):
                return redirect('homeMedico')
            else:
                messages.warning(self.request, 'Para ingresar a la página de administrador debes iniciar sesion primero')
                return redirect('loginAdmin')
            
        def get_queryset(self):
            curp = self.request.GET.get('curp', '')
            queryset = Medico.objects.filter(
                empleado_id__usuario_curp__curp__icontains = curp
            )
            return queryset

class ListarEncargadosFarmacia(ListView):
    template_name = 'gestion_admin/encargados.html'
    model = Encargado_farmacia
    context_object_name = 'encargados'
    
    
class ListarEncargadosPorID(ListView):
        template_name = 'gestion_admin/encargados.html'
        context_object_name = 'encargados'
        ## Válida que esté logeado un administrador
        def get(self, *args, **kwargs):
            if self.request.session.get('id_admin', False):
                return super().get(*args, **kwargs)
            elif self.request.session.get('id_encargado', False):
                return redirect('homefarmacia')
            elif self.request.session.get('id_medico', False):
                return redirect('homeMedico')
            else:
                messages.warning(self.request, 'Para ingresar a la página de administrador debes iniciar sesion primero')
                return redirect('loginAdmin')
            
        def get_queryset(self):
            curp = self.request.GET.get('curp', '')
            queryset = Encargado_farmacia.objects.filter(
                empleado_id__usuario_curp__curp__icontains = curp
            )
            return queryset
    