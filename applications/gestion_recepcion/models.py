from django.db import models

# Create your models here.

class Recepcionista(models.Model):
    empleado_id = models.ForeignKey('gestion_empleados.Empleado', on_delete=models.SET_NULL, null=True)