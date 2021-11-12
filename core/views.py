from django.shortcuts import redirect, render
from core.models import Evento


def lista_eventos(request):
    eventos = Evento.objects.all()
    response = {'eventos': eventos}
    return render(request, 'agenda.html', response)
