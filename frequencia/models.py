from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField(max_length=128)

    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

class Escala(models.Model):
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    turnos_validos = [('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno'), ('Extra', 'Extra')]
    turno = models.CharField(max_length=50, choices=turnos_validos, default='Matutino')

    def __str__(self):
        return 'hora inicio:'+str(self.hora_inicio)+' hora fim'+str(self.hora_fim) 

    class Meta:
        verbose_name = 'Escala'
        verbose_name_plural = 'Escalas'


class FuncEscala(models.Model):
    funcionario = models.ForeignKey(Funcionario, related_name='funcionarios', null=True, blank=False)
    escala = models.ForeignKey(Escala, related_name='escalas', null=True, blank=False)

    def __str__(self):
        return 'funcionario:'+str(self.funcionario)+' escala '+str(self.escala )

class Ponto(models.Model):
    data = models.TimeField()
    escalaFunc = models.ForeignKey(FuncEscala, related_name='frequencia', null=True, blank=False)
    chefe = models.ForeignKey(Funcionario, related_name='chefes', null=True, blank=False)
    tipo = models.CharField(max_length=50, choices=[('Entrada','Entrada'),('Saida','Saida')], default='Entrada')
    maquina = models.CharField(max_length=50)
    consistente = models.BooleanField()

class Justificativa(models.Model):
    data = models.DateTimeField()
    funcionario = models.ForeignKey(Funcionario, related_name='atrasados', null=True, blank=False)
    justificativa = models.CharField(max_length=255)
    ponto = models.OneToOneField(Ponto)
