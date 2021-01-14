from django.db import models

# Create your models here.

class Medico(models.Model):
    empleado_id = models.ForeignKey('gestion_empleados.Empleado', primary_key=True, on_delete=models.CASCADE)
    cedula_profesional = models.CharField(max_length=50)
    titular	= models.BooleanField()