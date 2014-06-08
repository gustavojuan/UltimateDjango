from django.db import models

# Create your models here.
class NombreEjemplo(models.Model):
    nombre = models.CharField(max_length=150)