from django.shortcuts import render
from django.http import HttpResponse

# View responsável pela tela inicial do médico - Temportário
def medico_view(request):
    print('Página funcionando!')
    return HttpResponse('Página inicial do médico')

# View responsável pela tela inicial do HOME - Temportário
def home(request):
    print('Home funcionando!')
    return HttpResponse('Home funcionando')

# começando a importar as URLs
