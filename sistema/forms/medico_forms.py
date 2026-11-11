from django.forms import forms
from sistema.models import Medico

# Checagem de e-mail -> O emailField do model já valida se é e-mail válido
# Checagem de senha -> 
# Checagem de dado inserido -> Dependendo do Field do atributo.

# Tupla - lista suspensa
ESPECIALIDADES = [
    ('CARDIOLOGIA', 'Cardiologia'),
    ('DERMATOLOGIA', 'Dermatologia'),
    ('GINECOLOGIA', 'Ginecologia'),
    ('NEUROLOGIA', 'Neurologia'),
    ('OFTALMOLOGIA', 'Oftalmologia'),
    ('ORTOPEDIA', 'Ortopedia'),
    ('PEDIATRIA', 'Pediatria'),
]

class MedicoForm(forms.ModelForm):
    
    # Troca o Charfield padrão por um <select> com opções fixas
    # Apenas para as especialidades
    especialidade = forms.ChoiceField( # Método do forms
        # Lista
        choices=[('', 'Selecione uma especialidade: ')] + ESPECIALIDADES, # Irá envolver com uma tupla / default / Concatenando com a lista suspensa
        label='Especialidade' # Chamando a especialidade
    )

    # APENAS NO PYTHON
    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm', 'especialidade', ]
        # criacao_data e ativo não aparecem, são preenchidos automaticamente
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'crm': 'CRM',
        }