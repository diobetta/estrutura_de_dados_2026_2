from django.forms import forms
from sistema.models import Paciente

# EXTRA: O professor não passou essa parte ainda

class PacienteForm(forms.ModelForm):
    "No model Paciente o CPF tem 11 caracteres, mas para o usuário podemos aceitar até 14"
    cpf = forms.CharField(
        label="CPF",
        max_lenght=14,
        help_text='Pode digitar com ou sem pontos e traço', # Isso aqui é extra, o professor não trabalhou em aula
        widget=forms.TextInput(attrs={'placeholder': '123.456.789-01', 'inputmode': 'numeric'}), # Isso aqui é extra, o professor não trabalhou em aula
    )

class Meta:
    model = Paciente
    fields = ['nome','sobrenome','cpf','email','telefone',] # Verificar sobre a imagem porque não foi cadastrada nos models
    labels = {
            "nome": "Nome",   
            "sobrenome": "Sobrenome",
            "email": "E-mail",
            "telefone": "Telefone",
            "cpf": "cpf",
            # O restante é preenchido automaticamente 
            # A imagem entraria aqui também
            }

    # Isso aqui também foi extra, o professor não trabalhou em aula
    help_texts = {'telefone': 'Com DDD, EX: (21) 99999-9999',}
    error_messages = {'email': {'invalid': 'Digite um e-mail válido, como nome@exemplo.com'},
                      'nome': {'required': 'Informe o nome do paciente'},
    }
    widgets = {'telefone': forms.TextInput (attrs={'placeholder': '(21) 99999-9999'})}