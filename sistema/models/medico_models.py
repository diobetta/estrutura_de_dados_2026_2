from django.db import models # ORM do Django para declarar modelos no banco de dados (NÃO É PYTHON)
from django.utils import timezone # Útil para gerar data/hora atual do projeto

# Modelo que representa um Paciente 
# Tabela
# Atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem/comentário, ativo(True/False)

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

    # método: identificação dos objetos que estão sendo criados
    # ele não mexe no portal do django, é apenas para o python -> não precisa mexer no migrations quando for mexer aqui
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'