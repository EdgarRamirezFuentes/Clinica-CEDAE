from django.contrib import admin
from .models import Encargado_farmacia
from .models import Medicamento
from .models import Ticket


# Register your models here.

admin.site.register(Encargado_farmacia)
admin.site.register(Medicamento)
admin.site.register(Ticket)