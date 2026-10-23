from django.db import models
class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=150)

class Meta:
    ordering = ["fecha", "hora"]

def __str__(self):
    return self.nombre

# Create your models here.
