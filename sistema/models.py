from django.db import models # ORM do Django para declarar modelos no banco de dados (NÃO É PYTHON)
from django.utils import timezone # Útil para gerar data/hora atual do projeto

# Modelo que representa um Paciente 
# Atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem/comentário, ativo(True/False)

class Paciente(models.Model):
    nome = models.CharField(max_length=25) # String em Python - Nome do paciente
    sobrenome = models.CharField(max_length=50) # Sobrenome do paciente
    email = models.EmailField() # Email de contato do paciente
    telefone = models.CharField(max_length=20) # Telefone de contato
    cadastro_data = models.DateTimeField(default=timezone.now) # Data/Hora de cadastro - Timezone: importar --- NÃO ESTÁ IGUAL AO DO PROFESSOR
    mensagem = models.TextField(blank=True) # blank=True > Pode ficar vazio
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica