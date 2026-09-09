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

    # método: identificação dos objetos que estão sendo criados
    # ele não mexe no portal do django, é apenas para o python -> não precisa mexer no migrations quando for mexer aqui
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

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
    
# Exercício 08/09: Criar um model para a consulta e linkar com o model médico

class Consulta(models.Model):

    # ForeignKey cria um relacionamento "muitos para um" (N:1) = Chave estrangeira

    # Relacionamento:
    # Dentro do parenteses, declara qual é o model. 
    # Ex: paciente_id = Paciente
    # Ex: medico_id = Medico

    # on_delete=CASCADE: se o paciente for deletado, todas as informações dele em outros models serão excluídas

    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id   = models.ForeignKey(Medico,   on_delete=models.CASCADE)

    data_consulta = models.DateTimeField(default=timezone.now)   # data/hora da consulta
    ativa         = models.BooleanField(default=True)            # campo de exclusão lógica 
    observacao    = models.TextField(blank=True)                 # anotação opcional

    # choices: lista de opções válidas para o campo
    # CharField: lista de tuplas (valor_no_banco, texto_exibido)
    status = models.CharField(
        default='A',    # valor padrão ao criar a consulta = Agendada
        max_length=1,   # salva apenas 1 caractere no banco (A, X, C ou R)
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )