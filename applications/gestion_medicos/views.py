from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
import datetime
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from ..gestion_usuarios.models import Usuario
from ..gestion_pacientes.models import Paciente, Cita
from ..gestion_pacientes.models import Receta
from ..gestion_pacientes.models import Cita
from ..gestion_pacientes.models import Consulta
from ..gestion_expediente.models import Expediente
from ..gestion_medicos.models import Medico
from ..gestion_farmacia.models import Medicamento
import hashlib

class Home(TemplateView):
    template_name = 'gestion_medicos/home.html'
    #model = Cita
    #context_object_name = 'citas'
    
    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')
        
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(medico_id_id=self.request.session['id_medico'],
                                               fecha=datetime.date.today()
                                               ).order_by('hora_inicio')
        return context

#def Calendar(request):
#    citas = Cita.objects.filter(medico_id_id=request.session['id_medico']).values()
#    citasJSON = json.dumps(list(citas), cls=DjangoJSONEncoder)
#    print(citasJSON)
#    return render(request, "gestion_medicos/calendar.html", {'citas' : citasJSON})

class Calendar(TemplateView):
    template_name = 'gestion_medicos/calendar.html'
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')

class listarPacientes(ListView):
    template_name = 'gestion_medicos/patients.html'
    model = Paciente
    context_object_name = 'pacientes'
    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')
    
class listarPacientePorID(ListView):
        template_name = 'gestion_medicos/patients.html'
        context_object_name = 'pacientes'
        ## Válida que esté logeado un médico
        def get(self, *args, **kwargs):
            if self.request.session.get('id_medico', False):
                return super().get(*args, **kwargs)
            elif self.request.session.get('id_encargado', False):
                return redirect('homefarmacia')
            else:
                messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
                return redirect('login')
            
        def get_queryset(self):
            curp = self.request.GET.get('curp', '')
            queryset = Paciente.objects.filter(
                idUsuario__curp__icontains = curp
            )
            return queryset
        
class verExpedientePaciente(TemplateView):
    template_name = 'gestion_medicos/medicalRecord.html'
    #model = Expediente
    #context_object_name = 'expediente'

    def get_context_data(self, **kwargs):
        context = super(verExpedientePaciente, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(paciente_id = self.kwargs.get('pk'))
        context['consultas'] = Consulta.objects.filter(expediente_id = self.kwargs.get('pk'))
        context['recetas'] = Receta.objects.filter()
        context['expediente'] = Expediente.objects.get(pk = self.kwargs.get('pk'))
        return context

    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')
    
class modificarExpediente(TemplateView):
    
    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')
        
    template_name = 'gestion_medicos/modifyMedicalRecord.html'
    def get_context_data(self, **kwargs):
        context = super(modificarExpediente, self).get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(pk = self.kwargs.get('pk'))
        context['expediente'] = Expediente.objects.get(pk = self.kwargs.get('pk'))
        return context
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            paciente = Paciente.objects.get(pk = self.kwargs.get('pk'))
            expediente = Expediente(
                    paciente_curp = paciente,
                    antecedentes_familiares = request.POST['antecedenteFamiliar'].strip(),
                    antecedentes_personales = request.POST['antecedentePersonal'].strip(),
                    examen_fisico = request.POST['examenFisico'].strip(),
                    alergias = request.POST['alergias'].strip(),
                    padecimiento_actual = request.POST['padecimiento'].strip(),
                    altura = float(request.POST['altura']),
                    presion_arterial = request.POST['presionArterial'],
                    saturacion_oxigeno = float(request.POST['oxigenacion']),
                    frecuencia_cardiaca = float(request.POST['frecuenciaCardiaca']),
                    frecuencia_respiratoria = float(request.POST['frecuenciaRespiratoria']),
                    temperatura = float(request.POST['temperatura']),
                    impresion_diagnostica = request.POST['impresionDiagnostica'].strip(),
                    peso = float(request.POST['peso']),
                    imc = round(float(request.POST['peso']) / pow(float(request.POST['altura']), 2), 2),
                )
            try:
                expediente.save()
                messages.success(request, 'Expediente modificado correctamente')
            except Exception as es:
                messages.error(request, 'Hubo un error al intentar modificar el expediente')
        return redirect('/medico/expediente-medico/'+ self.kwargs.get('pk'))

class verPerfilPaciente(DetailView):
    template_name = 'gestion_medicos/patientProfile.html'
    model = Paciente
    context_object_name = 'paciente'
    
    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')

class appointment(TemplateView):
    template_name = 'gestion_medicos/appointment.html'
    
    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')
    
    def get_context_data(self, **kwargs):
        context = super(appointment, self).get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(pk = self.kwargs.get('pk'))
        context['expediente'] = Expediente.objects.get(pk = self.kwargs.get('pk'))
        context['medicamentos'] = Medicamento.objects.filter()
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            expediente = Expediente(
                        paciente_curp = Paciente.objects.get(pk = self.kwargs.get('pk')),
                        antecedentes_familiares = request.POST['antecedenteFamiliar'],
                        antecedentes_personales = request.POST['antecedentePersonal'],
                        examen_fisico = request.POST['examenFisico'],
                        alergias = request.POST['alergias'],
                        padecimiento_actual = request.POST['padecimiento'],
                        altura = float(request.POST['altura']),
                        presion_arterial = request.POST['presionArterial'],
                        saturacion_oxigeno = float(request.POST['oxigenacion']),
                        frecuencia_cardiaca = float(request.POST['frecCardiaca']),
                        frecuencia_respiratoria = float(request.POST['frecRespiratoria']),
                        temperatura = float(request.POST['temperatura']),
                        impresion_diagnostica = request.POST['impresionDiagnostica'],
                        peso = float(request.POST['peso']),
                        imc = round(float(request.POST['peso']) / pow(float(request.POST['altura']), 2), 2),
                    )
            a = 'med'
            b = 'ind'
            recortado = ''
            listaMeds = []
            listaInst = []
            for x in range(1,15):
                if a+str(x) in request.POST:
                    recortado = request.POST[a+str(x)].split('|')[0]
                    listaMeds.append(recortado)
            for x in range(1,15):
                if b+str(x) in request.POST:
                    listaInst.append(request.POST[b+str(x)])
                    
            receta = Receta(
                    consulta_id = Consulta.objects.get(expediente_id_id = self.kwargs.get('pk')),
                    medico_id = Medico.objects.get(pk = self.request.session['id_medico']), ## Provisional en lo que se obtiene el id del médico
                    medicamentos = ' - '.join(listaMeds),
                    indicacion_medicamentos = ' - '.join(listaInst),
                )
            try:
                expediente.save()
                #messages.success(request, 'Se actualizo correctamente el expediente')
            except Exception as ex:
                messages.error(request, 'Hubo un error al tratar de actualizar el expediente')
            try:
                receta.save()
                messages.success(request, 'Se registró correctamente la receta')
            except Exception as ex:
                messages.error(request, 'Hubo un error al tratar de registrar la receta')
            print(request.POST['enviarCorreo'])
            if request.POST['enviarCorreo'] == 'on':
                medicamento = ''
                for x in range(0, len(listaMeds)):
                    medicamento = medicamento + str(x+1) + '. ' + listaMeds[x] + ': ' + listaInst[x] + '\n'
                
                medico = Medico.objects.get(pk = self.request.session['id_medico'])
                nombreMedico = ''
                nombreMedico = 'Dr. ' + medico.empleado_id.usuario_curp.nombre + ' ' + medico.empleado_id.usuario_curp.apellidoPaterno + ' ' + medico.empleado_id.usuario_curp.apellidoMaterno
                cedulaMedico = 'Cedula profesional: ' + medico.cedula_profesional

                fecha = str(date.today())

                paciente = Paciente.objects.get(pk = self.kwargs.get('pk'))

                nombrePaciente = paciente.idUsuario.nombre + ' ' + paciente.idUsuario.apellidoPaterno + ' ' + paciente.idUsuario.apellidoMaterno
                
                direccionClinica = 'Tuxpan 2 interior 902, colonia Roma Sur, Cuauhtémoc, Ciudad de México.' #provisional
                numeroClinica = 'Tel. 55 5264 2721' #provisional
                send_mail(
                    'Receta CEDAE',
                    'Esta es tu receta, \n \t\t\t'+ nombreMedico + '\n\t\t\t' + cedulaMedico + '\n' + 'Paciente: ' + nombrePaciente +'\t\tFecha: ' + fecha + '\n Medicamentos: \n' + medicamento + '\n \t' + direccionClinica + '\n \t\t\t\t' + numeroClinica,
                    settings.EMAIL_HOST_USER,
                    [request.POST.get('correoElec','')],
                    fail_silently = False,
                )
        return redirect('/medico/')
    
#def Patients(request):
#    # Barra de búsqueda de usuario
#    if request.method == 'POST':
#        patients = Paciente.objects.filter(idUsuario__contains=request.POST['curp'])
#        return render(request, 'gestion_medicos/patients.html', {'pacientes': patients})
#    patients = Paciente.objects.all().order_by('idUsuario')
#    return render(request, 'gestion_medicos/patients.html', {'pacientes': patients})


class RegisterPatient(TemplateView):
    template_name = 'gestion_medicos/registerPatient.html'
    ## Válida que esté logeado un médico
    def get(self, *args, **kwargs):
        if self.request.session.get('id_medico', False):
            return super().get(*args, **kwargs)
        elif self.request.session.get('id_encargado', False):
            return redirect('homefarmacia')
        else:
            messages.warning(self.request, 'Para ingresar a la página de médico debes iniciar sesion primero')
            return redirect('login')
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST['paciente'].strip() == "externo":
                # Registro de paciente desde 0
                usuario = Usuario(
                    curp = request.POST['curp'].strip(),
                    rfc = request.POST['rfc'].strip(),
                    nombre = request.POST['nombrePaciente'].strip(),
                    apellidoPaterno = request.POST['aPaternoPaciente'].strip(),
                    apellidoMaterno = request.POST['aMaternoPaciente'].strip(),
                    telefonoFijo = request.POST['telParticular'].strip(),
                    telefonoCelular = request.POST['telCelular'].strip(),
                    fechaNacimiento = request.POST['nacimiento'].strip(),
                    sexo = request.POST['genero'].strip(),
                    nacionalidad = request.POST['paises'].strip(),
                    estadoCivil = request.POST['estadoCivil'].strip(),
                    calle = request.POST['calle'].strip(),
                    numeroInterior = request.POST['numeroInterior'].strip(),
                    numeroExterior = request.POST['numeroExterior'].strip(),
                    colonia = request.POST['colonia'].strip(),
                    alcaldia = request.POST['alcaldia'].strip(),
                    estado = request.POST['estados'].strip(),
                    codigoPostal = request.POST['codigoPostal'].strip(),
                    nombreContactoEmergencia = request.POST['nombreEmergencia'].strip(),
                    apellidoPaternoContactoEmergencia = request.POST['aPaternoEmergencia'].strip(),
                    apellidoMaternoContactoEmergencia = request.POST['aMaternoEmergencia'].strip(),
                    telefonoContactoEmergencia = request.POST['telEmergencia'].strip(),
                    correo = request.POST['correo'].strip(),
                )
                
                paciente = Paciente(
                    idUsuario = usuario,
                    accesoExpediente = False,
                    accesoSistema = False
                )
                
                expediente = Expediente(
                    paciente_curp = paciente,
                    antecedentes_familiares = request.POST['antecedenteFamiliar'].strip(),
                    antecedentes_personales = request.POST['antecedentePersonal'].strip(),
                    examen_fisico = request.POST['examenFisico'].strip(),
                    alergias = request.POST['alergias'].strip(),
                    padecimiento_actual = request.POST['padecimiento'].strip(),
                    altura = float(request.POST['altura']),
                    presion_arterial = request.POST['presionArterial'],
                    saturacion_oxigeno = float(request.POST['oxigenacion']),
                    frecuencia_cardiaca = float(request.POST['frecuenciaCardiaca']),
                    frecuencia_respiratoria = float(request.POST['frecuenciaRespiratoria']),
                    temperatura = float(request.POST['temperatura']),
                    impresion_diagnostica = request.POST['impresionDiagnostica'].strip(),
                    peso = float(request.POST['peso']),
                    imc = round(float(request.POST['peso']) / pow(float(request.POST['altura']), 2), 2),
                )
                if not Usuario.objects.filter(curp=request.POST['curp']):
                    try:
                        usuario.save()
                        paciente.save()
                        expediente.save()
                        messages.success(request, 'Se registró correctamente el paciente')
                    except Exception as ex:
                        messages.error(request, 'Hubo un error al tratar de registrar al paciente', 'error')
                else:
                    messages.error(request, 'El CURP ingresado ya se encuentra registrado en el sistema.\nPuede que el paciente sea trabajador CEDAE', 'warining')
            else:
                # Registro de usuario CEDAE
                usuario = None
                try:
                    usuario = Usuario.objects.get(curp=request.POST['curp'])
                except Usuario.DoesNotExist as ex:
                    messages.error(request, 'El CURP ingresado no pertenece a ningún trabajador CEDAE')
                if usuario:
                    paciente = Paciente.objects.get(idUsuario=usuario)  
                    if paciente:
                        messages.warning(request, 'El CURP ingresado ya pertenece a un paciente')
                    else:
                        paciente = Paciente(
                            idUsuario = usuario,
                            accesoExpediente = False,
                            accesoSistema = False
                        )
                        
                        expediente = Expediente(
                            paciente_curp = paciente,
                            antecedentes_familiares = request.POST['antecedenteFamiliar'].strip(),
                            antecedentes_personales = request.POST['antecedentePersonal'].strip(),
                            examen_fisico = request.POST['examenFisico'].strip(),
                            alergias = request.POST['alergias'].strip(),
                            padecimiento_actual = request.POST['padecimiento'].strip(),
                            altura = float(request.POST['altura']),
                            presion_arterial = request.POST['presionArterial'],
                            saturacion_oxigeno = float(request.POST['oxigenacion']),
                            frecuencia_cardiaca = float(request.POST['frecuenciaCardiaca']),
                            frecuencia_respiratoria = float(request.POST['frecuenciaRespiratoria']),
                            temperatura = float(request.POST['temperatura']),
                            impresion_diagnostica = request.POST['impresionDiagnostica'].strip(),
                            peso = float(request.POST['peso']),
                            imc = round(float(request.POST['peso']) / pow(float(request.POST['altura']), 2), 2),
                        )
                        try:
                            paciente.save()
                            expediente.save()
                            messages.success(request, 'Se registró correctamente el paciente')
                        except Exception as ex:
                            messages.error(request, 'Hubo un error al tratar de registrar al paciente')
        return redirect('registerPatientMedico')            

class ActivarExpediente(TemplateView):
    def get(self, *args, **kwargs):
        usuario = Usuario.objects.get(pk=self.kwargs.get('pk'))
        paciente = Paciente.objects.get(pk = self.kwargs.get('pk'))
        paciente.accesoExpediente = True
        paciente.save()
        send_mail(
                'Acceso a expediente CEDAE',
                'Tu médico te ha otorgado acceso a tu expediente médico con éxito',
                settings.EMAIL_HOST_USER,
                [usuario.correo,],
                fail_silently = False,
        )
        messages.success(self.request, 'El acceso a expediente ha sido brindado con éxito')
        return redirect('patientProfileMedico', self.kwargs.get('pk'))

class ActivarCuenta(TemplateView):
    template_name = 'gestion_medicos/patientProfile.html'
    def get(self, *args, **kwargs):
        usuario = Usuario.objects.get(pk=self.kwargs.get('pk'))
        paciente = Paciente.objects.get(pk = self.kwargs.get('pk'))
        contrasenia = usuario.curp
        encoder = hashlib.new("sha1", str(contrasenia).encode('utf-8'))
        contrasenia = str(encoder.hexdigest()) 
        usuario.contrasenia = contrasenia
        usuario.save()
        paciente.accesoSistema = True
        paciente.save()
        send_mail(
                'Activación de cuenta CEDAE',
                'Tu cuenta CEDAE ha sido activada. \n Credenciales \n Correo: ' + usuario.correo + '\nContraseña: ' + usuario.curp,
                settings.EMAIL_HOST_USER,
                [usuario.correo,],
                fail_silently = False,
        )
        messages.success(self.request, 'La cuenta ha sido activada con éxito')
        return redirect('patientProfileMedico', self.kwargs.get('pk'))
    pass