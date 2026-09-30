# from django.contrib import admin
from django.urls import path
from sistema.views import medico_view

urlpatterns = [
    path('medico/', medico_view), #vollmed.online/medico
    path('medico/novo/'), #vollmed.online/medico/novo/
    path('medico/perfil/<int:medico_id>'), #vollmed.online/medico/perfil/
    path('medico/listagem/'), #vollmed.online/medico/listagem/
]