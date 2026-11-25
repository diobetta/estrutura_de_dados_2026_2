from django.shortcuts import render
from django.http import HttpResponse
from sistema.models import Medico

# VIEWS -> retornam algo, são funções (request -> response)
def medico_index(request):
    print('Página médico funcionando!')
    return HttpResponse('Página inicial do médico')

def medico_novo(request):
    print('Página médico funcionando!')
    return HttpResponse('Cadastrar novo médico')

def medico_listar(request):
    medicos = Medico.objects.filter(ativo=True).order_by('nome') # puxando o banco de dados do médico

    context = {
        'medicos': medicos,
    }

    return render(
        request,
        'medico/listagem_medico.html',
    )