# COMANDOS DO DJANGO

1. ``pip install django ``-> Instala o Django no projeto.
2. ``django-admin startproject nome_do_projeto .`` -> Criando um novo projeto em django.
3. ``python manage.py runserver`` -> Subindo o servidor.
4. ``python manage.py startapp nome_do_app`` -> Criando um novo app.
5. ``python manage.py migrate`` ->  Realiza as migrações(ativa) do projeto. Toda vez que for mexer no banco de dados, esse é o comando final.
6. ``python manage.py createsuperuser`` -> Cria um super usuário
7. ``python manage.py changepassword nomedousuario`` -> Altera a senha, caso você esqueça.
8. a) ``python manage.py makemigrations`` -> Cria/Gera um novo pacote de migração (útil para novo app e alteração no banco de dados). Ele prepara para o migrate.