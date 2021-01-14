from django.db import models

# Create your models here.

class Paciente(models.Model):
    idUsuario = models.ForeignKey('gestion_usuarios.Usuario', primary_key=True, on_delete=models.CASCADE)
    accesoExpediente = models.BooleanField(default=False)
    accesoSistema = models.BooleanField(default=False)
    medicos = models.ManyToManyField('gestion_medicos.Medico')

class Cita(models.Model):
    paciente_id = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    medico_id = models.ForeignKey('gestion_medicos.Medico', on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()

class Consulta(models.Model):
    cita_id = models.ForeignKey('Cita', on_delete=models.CASCADE)
    expediente_id = models.ForeignKey('gestion_expediente.Expediente', on_delete=models.CASCADE)
    costo = models.FloatField()
    motivo = models.CharField(max_length=200, default="motivo no especificado")
    esquema_corporal = models.ImageField()
    notas = models.CharField(max_length=500, default="ninguna nota")

class Receta(models.Model):
    consulta_id = models.ForeignKey('Consulta', on_delete=models.CASCADE)
    medico_id = models.ForeignKey('gestion_medicos.Medico', on_delete=models.CASCADE)
    medicamentos = models.CharField(max_length=1000)
    indicacion_medicamentos = models.CharField(max_length=1000)

