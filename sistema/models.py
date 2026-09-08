from django.db import models # ORM do Django para declarar modelos no banco de dados (NÃO É PYTHON)
from django.utils import timezone # Útil para gerar data/hora atual do projeto

# Modelo que representa um Paciente 
# Tabela
# Atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem/comentário, ativo(True/False)

class Paciente(models.Model): #no class aqui precisa ser Pascal Case, não em snake case
    nome = models.CharField(max_length=25) # Criando um campo de caracter > String em Python - Nome do paciente
    sobrenome = models.CharField(max_length=50) # Sobrenome do paciente
    email = models.EmailField() # Email de contato do paciente
    telefone = models.CharField(max_length=20) # Telefone de contato
    cadastro_data = models.DateTimeField(default=timezone.now) # Data/Hora de cadastro - Timezone: importar --- O ATRIBUTO NÃO ESTÁ IGUAL AO DO PROFESSOR
    mensagem = models.TextField(blank=True) # blank=True > Pode ficar vazio
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica

class Medico(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    data_cadastro_medico = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=20)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=25)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)