from django.shortcuts import render
# from django.http import HttpResponse -> utilizado quando não tem html criado ainda (renderização)
from sistema.models import Paciente # importando o objeto Paciente

# VIEWS -> retornam algo, são funções (request -> response)
def index(request):
    return render(
        request, 
        'global/base.html',
        ) #GLOBAL: Uma página inteira

# View responsável por listar todos os pacientes
def listar_pacientes(request):
    pacientes = Paciente.objects.all() # lista de objetos [obj1, obj2]

    context = { # dicionário
        'pacientes': pacientes,
    }

    return render(
        request, 
        'paciente/listar.html',
        context,
    )

