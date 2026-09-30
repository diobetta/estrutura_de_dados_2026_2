from django.shortcuts import render
from django.http import HttpResponse

# VIEWS -> retornam algo, são funções (request -> response)
def medico_view(request):
    print('Página médico funcionando!')
    return HttpResponse('Página inicial do médico')
