# COMANDOS DO DJANGO

1. ``pip install django ``-> Instala o Django no projeto.
2. ``django-admin startproject nome_do_projeto .`` -> Criando um novo projeto em django.
3. ``python manage.py runserver`` -> Subindo o servidor.
4. ``python manage.py startapp nome_do_app`` -> Criando um novo app.
5. ``python manage.py migrate`` ->  Realiza as migrações(ativa) do projeto.
 O resto está no google keep

 # Atividade
 1. Criar um model para o médico com as informações: 
 - Nome
 - Sobrenome
 - E-mail
 - Data da Criação
 - Telefone
 - CRM (6 digitos), será string
 - Especialidade 
 - Mensagem
 - Ativo = True

 2. Na Exibição do Portal administrativo, deverá ser apresentado:
 - Id, Nome, email, telefone, especialidade, crm, ativo 

# Atividade 
1. Criar um model para a consulta e linkar com o model médico (esta na apostila)