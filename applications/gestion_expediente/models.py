from django.db import models

# Create your models here.
class Expediente(models.Model):
    paciente_curp = models.ForeignKey('gestion_pacientes.Paciente', primary_key=True, on_delete=models.CASCADE)
    antecedentes_familiares = models.CharField(max_length=500)
    antecedentes_personales = models.CharField(max_length=500)
    examen_fisico = models.CharField(max_length=500)
    alergias = models.CharField(max_length=100)
    padecimiento_actual = models.CharField(max_length=100)
    altura = models.FloatField()
    presion_arterial = models.CharField(max_length=50)
    saturacion_oxigeno = models.FloatField()
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    temperatura = models.FloatField()
    impresion_diagnostica = models.CharField(max_length=500)
    peso = models.FloatField()
    imc  = models.FloatField()
    