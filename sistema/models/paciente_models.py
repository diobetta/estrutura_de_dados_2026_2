from django.db import models # ORM do Django para declarar modelos no banco de dados (NÃO É PYTHON)
from django.utils import timezone # Útil para gerar data/hora atual do projeto

# Modelo que representa um Paciente 
# Tabela
# Atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem/comentário, ativo(True/False)

class Paciente(models.Model): #no class aqui precisa ser Pascal Case, não em snake case
    nome = models.CharField(max_length=25) # Criando um campo de caracter > String em Python - Nome do paciente
    sobrenome = models.CharField(max_length=50) # Sobrenome do paciente
    cpf = models.CharField(max_length=11) # CPF com 11 dígitos, sem traço e sem ponto
    email = models.EmailField() # Email de contato do paciente
    telefone = models.CharField(max_length=20) # Telefone de contato
    cadastro_data = models.DateTimeField(default=timezone.now) # Data/Hora de cadastro - Timezone: importar --- O ATRIBUTO NÃO ESTÁ IGUAL AO DO PROFESSOR
    mensagem = models.TextField(blank=True) # blank=True > Pode ficar vazio
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica

    # método: identificação dos objetos que estão sendo criados
    # ele não mexe no portal do django, é apenas para o python -> não precisa mexer no migrations quando for mexer aqui
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'