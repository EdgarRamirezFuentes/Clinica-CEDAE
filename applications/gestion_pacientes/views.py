from django.shortcuts import render

# Create your views here.

class Home(TemplateView):
    template_name = 'gestion_pacientes/home.html'

class verPerfil(DetailView):
    template_name = 'gestion_pacientes/perfil.html'
    model = Paciente
    context_object_name = 'paciente'

class verExpediente(TemplateView):
    template_name = 'gestion_pacientes/verexpediente.html'

    def get_context_data(self, **kwargs):
        context = super(verExpedientePaciente, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(paciente_id = self.kwargs.get('pk'))
        context['consultas'] = Consulta.objects.filter(expediente_id = self.kwargs.get('pk'))
        context['recetas'] = Receta.objects.filter()
        context['expediente'] = Expediente.objects.get(pk = self.kwargs.get('pk'))
        