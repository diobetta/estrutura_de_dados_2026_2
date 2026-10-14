from django.forms import forms
from sistema.models import * # importa os models do sistema

# Checagem de e-mail
# Checagem de senha
# Checagem de dado inserido

# DÁ PRA IMPORTAR TUDO DE UMA VEZ, MAS NÃO DÁ PRA FAZER ISSO NO JAVA
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        # a lista pode ser alterada
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm',]