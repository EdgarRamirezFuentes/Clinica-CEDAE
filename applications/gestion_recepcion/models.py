from django.db import models

# Create your models here.

class Recepcionista(models.Model):
    empleado_id = models.ForeignKey('gestion_empleados.Empleado', primary_key=True, on_delete=models.CASCADE)