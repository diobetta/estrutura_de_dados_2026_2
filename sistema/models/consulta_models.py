from django.db import models # ORM do Django para declarar modelos no banco de dados (NÃO É PYTHON)
from django.utils import timezone # Útil para gerar data/hora atual do projeto

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