from django.shortcuts import render
from django.http import HttpResponse

# VIEWS -> retornam algo, são funções (request -> response)
def consulta_view(request):
    print('Página consulta funcionando!')
    return HttpResponse('Página inicial da consulta')
