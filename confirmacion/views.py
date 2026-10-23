from django.shortcuts import render

from .forms import FormularioCedula
from .servicios import buscar_invitaciones

def confirmar(request):
    invitaciones = None # None = todavía no se ha buscado nada
    if request.method == "POST":
        formulario = FormularioCedula(request.POST)
        if formulario.is_valid():
            invitaciones = buscar_invitaciones(formulario.cleaned_data["cedula"])
    else:
        formulario = FormularioCedula()
    contexto = {"formulario": formulario, "invitaciones": invitaciones}
    return render(request, "confirmacion/confirmar.html", contexto)
