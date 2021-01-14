from django.db import models

# Create your models here.

class Empleado(models.Model):
    usuario_curp = models.ForeignKey('gestion_usuarios.Usuario', primary_key=True, on_delete=models.CASCADE)
    dias_laborales = models.CharField(max_length=7)
    hora_entrada = models.TimeField(auto_now=False, auto_now_add=False)
    hora_salida = models.TimeField(auto_now=False, auto_now_add=False)
    activo = models.BooleanField(default=False)
    hora_descanso = models.TimeField(auto_now=False, auto_now_add=False)