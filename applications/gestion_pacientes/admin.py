from django.contrib import admin
from .models import Paciente
from .models import Cita
from .models import Consulta
from .models import Receta

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Consulta)
admin.site.register(Receta)
