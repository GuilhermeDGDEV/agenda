from django.contrib.auth import decorators
from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario or usuario.username == 'admin':
        evento.delete()
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}

    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)

    return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user

    if usuario.username == 'admin':
        eventos = Evento.objects.all()
    else:
        eventos = Evento.objects.filter(usuario=usuario)

    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        id_evento = request.POST.get('id_evento')

        usuario = request.user

        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
        else:
            Evento.objects.create(
                titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return redirect('/')
