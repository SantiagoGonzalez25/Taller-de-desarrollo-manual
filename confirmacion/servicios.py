from invitados.models import Invitado

def buscar_invitaciones(cedula):
    invitaciones = (
        Invitado.objects.filter(cedula=cedula)
        .select_related("evento")
        .order_by("evento__fecha", "evento__hora")
    )
    
    return list(invitaciones)