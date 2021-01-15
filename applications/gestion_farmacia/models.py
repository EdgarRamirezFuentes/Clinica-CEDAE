from django.db import models

# Create your models here.

class Encargado_farmacia(models.Model):
    empleado_id = models.ForeignKey('gestion_empleados.Empleado', primary_key=True, on_delete=models.CASCADE)

class Medicamento(models.Model):
    sku = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    sustancia_activa = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=30)
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=0)
    fecha_caducidad = models.DateField()

#class Ticket(models.Model):
    
 #   fecha_expedicion = models.DateField(auto_now=True, auto_now_add=True)
  #  costo_total = models.FloatField()
   # pass