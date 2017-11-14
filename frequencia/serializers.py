from rest_framework import routers, serializers, viewsets
from frequencia.models import *

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
        
    def create(self, data):
        funcionario = Funcionario.objects.create(**data)
        return funcionario

class EscalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escala
        fields = '__all__'

    def create(self, data):
        escala = Escala.objects.create(**data)
        return escala
        
class FuncEscalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FuncEscala
        fields = ('funcionario','escala')
        
    def create(self, data):
        func_escala = FuncEscala.objects.create(**data)
        return func_escala

class PontoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ponto
        fields = '__all__'

    def create(self, data):
        func_escala = FuncEscala.objects.create(**data)
        return func_escala
    
class JustificativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Justificativa
        fields = '__all__'

    def create(self, data):
        justificativa = Justificativa.objects.create(**data)
        return justificativa
