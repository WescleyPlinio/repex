# Repositório de Propostas e projetos de Ensino, Pesquisa e Extensão - REPEX
Para usar o sistema, siga esses passos:

### Após baixar o projeto, ative a venv e instale as dependências:

    pip install -r requirements.txt

### Após isso faça:

    py manage.py loaddata repex/fixtures/areas_conhecimento.json

    py manage.py loaddata repex/fixtures/projetos.json

    py manage.py loaddata repex/fixtures/noticias.json

### Por fim, rode:

    py manage.py runserver