from django.db import models

# Create your models here.
class Administrador(models.Model):
    usuario = models.CharField(max_length=50, primary_key=True)
    contrasenia = models.CharField(max_length=100)
    