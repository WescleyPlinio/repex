# Repositório de Propostas e projetos de Ensino, Pesquisa e Extensão - REPEX
Para usar o sistema, siga esses passos:

### Após baixar o projeto, ative a venv e instale as dependências:

    pip install -r requirements.txt

### Após isso faça as migrações:
    py manage.py migrate

### Instale objetos prontos (opcional, mas se instalar precisa ser nessa ordem):

    py manage.py loaddata repex/fixtures/areas_conhecimento.json
    py manage.py loaddata users/fixtures/users.json
    py manage.py loaddata repex/fixtures/projetos.json
    py manage.py loaddata repex/fixtures/noticias.json

### Crie um super usuário:

    py manage.py createsuperuser

### Por fim, rode:

    py manage.py runserver