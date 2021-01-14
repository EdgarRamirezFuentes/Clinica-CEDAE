from django.contrib import admin
from .models import Expediente

# Register your models here.
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ( 'paciente_curp',)
    search_fields = ('paciente_curp',)
    
admin.site.register(Expediente, MedicalRecordAdmin)