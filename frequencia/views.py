from django.shortcuts import render
from django.contrib.auth.models import User
from frequencia.models import *
from frequencia.serializers import *


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer

    
class FuncEscalaViewSet(viewsets.ModelViewSet):
    queryset = FuncEscala.objects.all()
    serializer_class = FuncEscalaSerializer


class PontoViewSet(viewsets.ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer

class JustficativaViewSet(viewsets.ModelViewSet):
    queryset = Justificativa.objects.all()
    serializer_class = JustificativaSerializer
