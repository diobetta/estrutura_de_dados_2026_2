from django.contrib import admin
from django.urls import path, include
# VIEWS -> retornam algo, são funções, request -> response

# COMEÇANDO A IMPORTAR VIEWS
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home), > depois será mexido
    path('', include('sistema.urls.py')), # Chamando as URLs do app Sistema -> Depois de logado
    # Preciso chamar as URLs do app Portal -> Home, cadastro, login
]

# CAMINHOS DAS URLS - FLUXO DE NAVEGAÇÃO

# www.vollmed.online/
# www.vollmed.online/login
# www.vollmed.online/

# LOGIN - MEDICO
# www.vollmed.online/medico/(o ID do medico irá entrar aqui)/ -> Perfil do MEDICO
# www.vollmed.online/medico/id-medico/alterar -> Alterar cadastro do médico

# www.vollmed.online/medico/id-medico/consultas -> Irá visualizar as consultas que ele tem disponíveis

# LOGIN - PACIENTE
# 1. www.vollmed.online/paciente/(o ID do paciente irá entrar aqui)/ -> Perfil do PACIENTE
# 2. www.vollmed.online/paciente/id-paciente/alterar -> Alterar cadastro do PACIENTE

# 3. www.vollmed.online/paciente/id-paciente/consulta/ -> visualizar consultas
# 4. www.vollmed.online/paciente/id-paciente/consulta/cadastrar/ -> cadastrar consulta
# 5. www.vollmed.online/paciente/id-paciente/consulta/id-consulta/ -> visualizar uma consulta específica
# 6. www.vollmed.online/paciente/id-paciente/consulta/id-consulta/alterar/ -> alterar consulta

# CONSULTA (nesse sistema não terá login para SECRETARIO / RECEPCIONISTA)