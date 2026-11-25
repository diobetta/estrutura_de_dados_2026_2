# from django.contrib import admin
from django.urls import path
from sistema.views import medico_index
from sistema.views import medico_novo
from sistema.views import medico_listar

urlpatterns = [
    path('medico/', medico_index), #vollmed.online/medico    
    path('medico/novo/', medico_novo, name='medico-create'), #vollmed.online/medico/novo/
    path('medico/listagem/', medico_listar, name='medico-list'), #vollmed.online/medico/listagem/
    # path('medico/perfil/<int:medico_id>'), #vollmed.online/medico/perfil/

]