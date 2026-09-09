from django.contrib import admin
from sistema import models

# Anotação dentro de um framework automatico - ORM
@admin.register(models.Paciente) # Registrando a classe Paciente no Portal do Python > Django
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin): # Registrando a classe Médico no Portal do Python > Django
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'crm', 'ativo', )
    
# Exercício 08/09: Criar um model para a consulta e linkar com o model médico

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    # paciente_id e medico_id são ForeignKeys: o admin exibe o __str__ deles
    list_display = ('id', 'paciente_id', 'medico_id', 'status',)