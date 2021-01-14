from django.db import models

# Create your models here.

class Usuario(models.Model):
    curp = models.CharField(max_length=18, primary_key=True)
    rfc = models.CharField(null=True, max_length=13)
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    telefonoCelular = models.CharField(max_length=20)
    telefonoFijo = models.CharField(max_length=20)
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
    sexo = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    estadoCivil = models.CharField(max_length=50)
    calle = models.CharField(max_length=100)
    numeroInterior = models.CharField(max_length=50)
    numeroExterior = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    alcaldia = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigoPostal = models.CharField(max_length=5)
    nombreContactoEmergencia = models.CharField(max_length=100)
    apellidoPaternoContactoEmergencia = models.CharField(max_length=100)
    apellidoMaternoContactoEmergencia = models.CharField(max_length=100)
    telefonoContactoEmergencia = models.CharField(max_length=20, default=None)
    correo = models.EmailField(max_length=254)
    contrasenia = models.CharField(max_length=100)
    
    def __str__(self):
        return self.curp