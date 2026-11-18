from django.forms import forms
from sistema.models import Paciente

# EXTRA: O professor não passou essa parte ainda

class PacienteForm(forms.ModelForm):
    cpf = forms.CharField(
        label='CPF',
        max_lenght=14,
        help_text='Pode digitar com ou sem pontos e traço',
        widget=forms.TextInput(attrs={'placeholder': '123.456.789-01', 'inputmode': 'numeric'}),
    )

class Meta:
    model = Paciente
    fields = ['nome','sobrenome','cpf','email','telefone'] # Verificar sobre a imagem porque não foi cadastrada nos models
    labels = {'nome': 'Nome',
              'sobrenome': 'Sobrenome',
              'email': 'E-mail',
              'telefone': 'Telefone' 
              # A imagem entraria aqui também
              }
    help_texts = {'telefone': 'Com DDD, EX: (21) 99999-9999',}
    error_messages = {'email': {'invalid': 'Digite um e-mail válido, como nome@exemplo.com'},
                      'nome': {'required': 'Informe o nome do paciente'},
    }
    widgets = {'telefone': forms.TextInput (attrs={'placeholder': '(21) 99999-9999'})}