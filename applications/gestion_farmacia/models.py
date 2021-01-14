from django.db import models

# Create your models here.

class Encargado_farmacia(models.Model):
    empleado_id = models.ForeignKey('gestion_empleados.Empleado', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.empleado_id.id