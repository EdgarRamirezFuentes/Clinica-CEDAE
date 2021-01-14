from django.contrib import admin
from .models import Usuario
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ( 'curp','nombre', 'apellidoPaterno', 'apellidoMaterno', 'correo')
    search_fields = ('curp',)
    list_filter = ('curp',)
    
admin.site.register(Usuario,UserAdmin)