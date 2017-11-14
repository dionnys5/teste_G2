from django.contrib import admin

# Register your models here.
from frequencia.models import Funcionario, Escala, Ponto, FuncEscala, Justificativa

admin.site.register(Funcionario)
admin.site.register(Escala)
admin.site.register(Ponto)
admin.site.register(FuncEscala)
admin.site.register(Justificativa)
