from django.contrib import admin
from sistema import models

# Anotação dentro de um framework
@admin.register(models.Paciente) # Registrando a classe Paciente no Portal do Python > Django
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin): # Registrando a classe Médico no Portal do Python > Django
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'crm', 'ativo', )