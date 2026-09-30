# from django.contrib import admin
from django.urls import path
from sistema.views import *

urlpatterns = [
    path('paciente/', index), #vollmed.online/paciente
    path('paciente/novo/'), #vollmed.online/paciente/novo/
    path('paciente/perfil/<int:paciente_id>'), #vollmed.online/paciente/perfil/ path variable
    path('paciente/listagem/', listar_pacientes), #vollmed.online/paciente/listagem/ importou a listagem de pacientes
]