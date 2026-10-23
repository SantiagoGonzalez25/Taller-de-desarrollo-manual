from django.db import models

from eventos.models import Evento

class Invitado(models.Model):
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name="invitados"
    )
    nombre = models.CharField("Nombres", max_length=150)
    cedula = models.CharField("Cédula (CC)", max_length=15)

    class Meta:
        unique_together = ("evento", "cedula")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
