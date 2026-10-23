from django.shortcuts import get_object_or_404, render

from .models import Evento

def lista(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/lista.html", {"eventos": eventos})

def detalle(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, "eventos/detalle.html", {"evento": evento})
