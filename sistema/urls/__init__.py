# importando os arquivos URLs
from .paciente_urls import urlpatterns as paciente_urlpatterns
from .medico_urls import urlpatterns as medico_urlpatterns
from .consulta_urls import urlpatterns as consulta_urlpatterns

app_name = 'sistema' # namespace, utilizado dentro dos templates

urlpatterns = paciente_urlpatterns + medico_urlpatterns + consulta_urlpatterns