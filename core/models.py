from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(null=True, verbose_name="Descrição do evento")
    data_evento = models.DateTimeField(verbose_name="Data do evento")
    data_criacao = models.DateTimeField(
        auto_now=True, verbose_name="Data da criação")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
